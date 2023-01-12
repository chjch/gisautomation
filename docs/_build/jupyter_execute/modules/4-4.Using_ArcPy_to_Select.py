#!/usr/bin/env python
# coding: utf-8

# # 4-4: Selection in ArcPy
# 
# ## 1. Selection Query
# 
# ### 1.1 SQL (structured query language) expression
# 
# **Expression**: `<field name> <logic operator> <value>`
# 
# ![SQL exp](https://pro.arcgis.com/en/pro-app/latest/help/mapping/navigation/GUID-F131B6FC-4650-4EFD-B2BE-4C500E5E5A94-web.png)
# 
# Referenes:
# 
# - [SQL reference for query expressions used in ArcGIS](http://pro.arcgis.com/en/pro-app/help/mapping/navigation/sql-reference-for-elements-used-in-query-expressions.htm)
# - [Specifying a query in Python](http://pro.arcgis.com/en/pro-app/arcpy/get-started/specifying-a-query.htm)
# 
# Let's work on two examples using the `zip_bounaries` feature class:
# 
# - numeric value: `POP2010 > 10000`
# - text value: `PO_NAME = Gainesville`

# ``` {admonition} 📝 Notes for specifying SQL with ArcPy:
# - Query in ArcPy functions is supplied as a **Python string**.
# - **Field delimiter** must be used to denote a field in the query. 
#     - `"field"`: a _shapefile_ or a _feature class_ in a **_file geodatabase_**
#     - `[field]`: a _feature class_ in a **_personal geodatabase_**
# - **Text value** must always be enclosed in <u>single quotes</u>.
# ```

# ```
# " "     # double quote
# ' '     # single quote
# """ """ # triple quotes
# '\'     # escape character
# ```

# ### 1.2 Build SQL query with triple quotes

# In[1]:


# numeric value
print(""""POP2010" > 10000""")


# In[2]:


# text value
print(""""PO_NAME" = 'GAINESVILLE'""")


# ### 1.3 Build SQL query with escape character

# In[3]:


print("\"")
print("\'")


# In[4]:


query_numeric = "\"POP2010\" > 10000"
print(query_numeric)


# In[5]:


query_text = "\"PO_NAME\" = \'GAINESVILLE\'"
print(query_text)


# ### 1.4 Build SQL query with `.format` string

# In[6]:


query_numeric = "{} > {}".format('"POP2010"', 10000)
print(query_numeric)


# In[7]:


query_text = "{} = {}".format('"PO_NAME"', "'GAINESVILLE'")
print(query_text)


# ### 1.5 Create query with compound criterion
# 
# - population greater than 10,000 **AND** name equals to gainesville
# - population greater than 10,000 **OR** name equals to gainesville

# In[8]:


query_comp = "{} > {} AND {} = {}".format('"POP2010"', 10000, '"PO_NAME"', "'GAINESVILLE'")
print(query_comp)


# In[9]:


query_comp = "{} > {} OR {} = {}".format('"POP2010"', 10000, '"PO_NAME"', "'GAINESVILLE'")
print(query_comp)


# ## 2. `Select` Function
# 
# [This function](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/select.htm)
# Extracts features from an input feature class or input feature layer, typically
# using a select or Structured Query Language (SQL) expression, and **stores**
# them in an output feature class, i.e., saves on the drive.

# In[10]:


import arcpy


# In[11]:


gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp


# In[12]:


zip_fc = "zip_boundaries"


# In[13]:


query_numeric = """"POP2010" > 10000"""
zip_output = "zipbnd_q1"
arcpy.Select_analysis(zip_fc, zip_output, query_numeric)


# In[28]:


query_text = "\"PO_NAME\" = \'GAINESVILLE\'"
zip_output = "zipbnd_q2"
arcpy.analysis.Select(zip_fc, zip_output, query_text)


# In[30]:


# arcpy.env.overwriteOutput = True
query_comp = "{} > {} AND {} = {}".format('"POP2010"', 10000, '"PO_NAME"', "'GAINESVILLE'")
zip_output = "zipbnd_q2"
arcpy.analysis.Select(zip_fc, zip_output, query_comp)


# ## 3. Select by Attributes

# In[31]:


zip_fc = "zip_boundaries"
query_numeric = """"POP2010" > 10000"""
zip_lyr = arcpy.management.SelectLayerByAttribute(zip_fc, "NEW_SELECTION", query_numeric)


# In[32]:


print(arcpy.GetCount_management(zip_lyr))


# ```{admonition} 🧭**Pro Tip**:
# 
# Select by attribute and Select by location introduced later only **temporarily**
# select features out of the specified feature class, meaning they
# **don't physically save files** on the hard disk of your computer.
# 
# Therefore, it is a good idea to save the output as a variable to be able to
# reference the selection later in the codes. 

# ## 4. Select by Location

# In[33]:


blkgrp_fc = "blockgroups"
cntbnd_fc = "county_boundary"
blkgrp_lyr = arcpy.management.SelectLayerByLocation(blkgrp_fc, "WITHIN", cntbnd_fc, "", "", "")


# In[34]:


print(arcpy.management.GetCount(blkgrp_fc))


# In[35]:


print(arcpy.GetCount_management(blkgrp_lyr))


# ## 5. Save Selection to a Feature Class
# 
# There are two options to save a "temporary" selection to an output layer.
# It is critical to understand how to set output **path** and **name** in each
# of the method.
# 
# - `arcpy.conversion.FeatureClassToFeatureClass(<path>, <fc name>)`
# - `arcpy.management.CopyFeatures()`
#     - without a path: create feature class in current workspace
#     - with specified path:
#         - use `"\\"` to concatenate path and name
#         - use `os.path.join()` function
#         - define the full path name altogether

# 

# In[38]:


output_path = r"..\data\class_data.gdb"
output_fc = "blockgroups_I75_2mi"


# In[39]:


arcpy.conversion.FeatureClassToFeatureClass(blkgrp_lyr, output_path, output_fc)


# In[40]:


# ouptut not specified
arcpy.management.CopyFeatures(blkgrp_lyr)


# In[41]:


output_path + "\\" + output_fc


# In[42]:


import os
output_name = os.path.join(output_path, output_fc)
output_name


# In[43]:


output_name = r'..data\class_data.gdb\module1\FirstModelBuilder\FirstModelBuilder.gdb\blockgroups_I75_2mi'

