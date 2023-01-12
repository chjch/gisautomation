#!/usr/bin/env python
# coding: utf-8

# # 4-3: Run ArcPy Functions

# ## 1. `ListFeatureClasses()`
# 
# [The function](https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/listfeatureclasses.htm)
# returns a list of the feature classes in the current workspace, which can be
# further filtered by specifying **_name_**, **_feature type_**, and
# **_feature dataset_** as optional arguments.
# 
# ### 1.1 Basic setting

# In[1]:


import arcpy


# In[2]:


gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp


# In[3]:


arcpy.ListFeatureClasses()


# ```{admonition} Note:
# The `workspace` environment must be set before using the list function.
# ```

# ### 1.2 Optional keyword arguments
# 
# - `wild_card`: a string with an asterisk 
# - `feature_type`: a string indicating feature type, i.e., _Point_, _Line_, _Polygon_
# - `feature_dataset`: a string that is the name of the feature dataset.

# In[4]:


arcpy.ListFeatureClasses("major*")


# In[5]:


arcpy.ListFeatureClasses("*roads")


# ### 1.3 Supply arguments to Python functions
# 
# - by order:
#   - skip the argument if using default by either **empty string** or `None`.
# - by keyword:
#   - the order of arguments doesn't matter if using keyword

# In[6]:


# by order with empty string
arcpy.ListFeatureClasses("", "Line")


# In[7]:


# by order with None object
arcpy.ListFeatureClasses(None, "Point")


# ``` {admonition} Note:
# `None` is a Python object not a string.
# ```

# In[8]:


type(None)


# In[9]:


# specifying both arguments by order
arcpy.ListFeatureClasses("*s", "Point")


# In[10]:


# no space around the assignment operator when assign value to argument (PEP8)
arcpy.ListFeatureClasses(feature_type="Point") # skipped the first argument


# In[11]:


# no need to supply in sequence if using keyword
arcpy.ListFeatureClasses(feature_type="Point", wild_card="*s") 


# In[12]:


arcpy.ListFeatureClasses(feature_type="Polygon") 


# In[13]:


# return empty list if no match found in the workspace
arcpy.ListFeatureClasses(feature_dataset="test")


# ## 2. Buffer

# In[14]:


I75 = "I75"
I75_buff = "I75_2mile_buff"
arcpy.Buffer_analysis(I75, "I75_2mile_buff", "2 Miles")


# ```{admonition} Pro Tip:
# Create variables for **arguments**, especially for the _input_ and _output_ feature class.
# ```

# ## 3. Clip

# In[ ]:


school = "schools"
school_2mile_I75 = "schools_2mile_I75"
arcpy.analysis.Clip(school, I75_buff, school_2mile_I75)


# ## 4. Spatial Join

# In[51]:


blkgrp = "blockgroups"
bg_school_spjoin = "blockgroups_school_spjoin"
arcpy.SpatialJoin_analysis(blkgrp, school_2mile_I75, bg_school_spjoin, "", "KEEP_COMMON") # keep common as the join type


# In[53]:


# count number of census block groups that match critieria
print(arcpy.GetCount_management(bg_school_spjoin))


# ## 5. Add Exception Handling
# 
# ```
# try:
#     arcpy.Toolname_toolboxalias
# except Exception as e:
#     print(e)
# ```

# In[ ]:


try:
    blkgrp = "blockgroups"
    bg_school_spjoin = "blockgroups_school_spjoin"
    arcpy.SpatialJoin_analysis(blkgrp, school_2mile_I75, bg_school_spjoin, "", "KEEP_COMMON")
    arcpy.GetCount_management(bg_school_spjoin)
except Exception as e:
    print("Error: " + str(e)) #.strip())


# ### 5.1 Detect feature class existance
# 
# As seen in the above cell, if the output feature class already exists in a
# workspace, by default, ArcPy will complain and stop executing the function.
# 
# In this situation we can use `arcpy.Exist` to detect the existance of a feature
# class first, if already exists, use `arcpy.management.Delete` to **delete** it.

# In[ ]:


if arcpy.Exists(bg_school_spjoin):
    print("A feature class with the name {} already exists".format(bg_school_spjoin))
    arcpy.Delete_management(bg_school_spjoin)
    print("However, arcpy helped you deleted {}.".format(bg_school_spjoin))
try:
    blkgrp = "blockgroups"
    bg_school_spjoin = "blockgroups_school_spjoin"
    arcpy.SpatialJoin_analysis(blkgrp, school_2mile_I75, bg_school_spjoin, "", "KEEP_COMMON")
    print("succeed, output {} features".format(arcpy.GetCount_management(bg_school_spjoin)))
except Exception as e:
    print("Error: " + str(e).strip())


# ### 5.2 Set the `OverwriteOutput` attribute of the `env` class
# 
# Another option is to simply set `OverwriteOutput` to be `True`.
# However, be careful, enable this setting will cause ArcPy to always overwrite
# current feature class to write output feature class.

# In[ ]:


arcpy.env.overwriteOutput = True
if arcpy.Exists(bg_school_spjoin):
    print("Yes, {} exists".format(bg_school_spjoin))
try:
    blkgrp = "blockgroups"
    bg_school_spjoin = "blockgroups_school_spjoin"
    arcpy.SpatialJoin_analysis(blkgrp, school_2mile_I75, bg_school_spjoin, "", "KEEP_COMMON")
    print("succeed, output {} features".format(arcpy.GetCount_management(bg_school_spjoin)))
except Exception as e:
    print("Error: " + str(e).strip())

