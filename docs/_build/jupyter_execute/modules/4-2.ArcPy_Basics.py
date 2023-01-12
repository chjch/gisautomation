#!/usr/bin/env python
# coding: utf-8

# # 4-2: Introduction to ArcPy
# 
# ## Part 1 - ArcPy Settings 

# ```{admonition} What is ArcPy?
# ArcPy is a Python site package that provides a useful and productive way to perform:
# 
# - geographic data analysis,
# - data conversion,
# - data management,and
# - map automation
# 
# with Python.
# ```
# 
# - [Essential ArcPy Vocabulary](https://pro.arcgis.com/en/pro-app/2.8/arcpy/get-started/essential-arcpy-vocabulary.htm)
# - [A quick tour of ArcPy](https://pro.arcgis.com/en/pro-app/2.8/arcpy/get-started/a-quick-tour-of-arcpy.htm)
# - [Python in ArcGIS Pro](https://pro.arcgis.com/en/pro-app/2.8/arcpy/get-started/installing-python-for-arcgis-pro.htm)

# ## 1. ArcPy Workspace
# 
# ### 1.1 Import the package

# In[1]:


import arcpy


# ### 1.2 ArcGIS Workspace
# 
# In ArcGIS, a workspace is a **container** for **_geographic data_**. A workspace can be a _folder_ that contains shapefiles, a _geodatabase_, a _feature dataset_, or an _ArcInfo workspace_. 
# 
# To reference a workspace, one needs to specify the **path to the directory** where the workspace is located.
# 
# ``` {admonition} ✒️ Ways to quickly grab a path
# 1. In File Explorer: `shift + right click` -> copy as path
# 2. In ArcGIS Pro: Map Tab -> Clipboard -> Copy Path ![copy path](https://pro.arcgis.com/en/pro-app/latest/help/projects/GUID-E1EBAAF8-8264-4357-98F1-35B9E6DEEC6C-web.png)
# (Only works when a workspace/dataset is selected in _Catalog Pane_)
# ```

# ### 1.3 Working with paths
# 
# The above methods copy the path with a backslash, i.e., `\` as the delimiter
# between a parent folder and a sub-folder, which is in conflict with the
# **escape character** of Python.
# 
# There are three options to address this:
# 
# 1. Change the delimiter to be double backslashes, i.e., `\\`
# 2. Change the delimiter to be a single forwardslash, i.e., `/`
# 3. Change the string to a raw string with a `r` in front of the path.

# In[2]:


print("..\\data\\class_data.gdb") # double backslashes


# In[3]:


print("../data/class_data.gdb") # single forward slash


# In[4]:


print(r"../data/class_data.gdb") # raw string


# In[5]:


print('C:\Albert Gator\URP6271\class_data.gdb\major_roads')


# ```{warning}
# Path names with spaces in them must be called with an 'r' and double qoutes
# ```

# ``` {admonition} 📝 **Escape sequence to remember**
# 
# - `\\` --> backslash (\)
# - `\"` --> double quote
# - `\'` --> single quote
# - `\n` --> line feed (start a new line)
# - `\t` --> a Tab (**eight** spaces by default in Python)
# 
# [more escape sequence](https://docs.python.org/3/reference/lexical_analysis.html\#index-22)
# ```

# In[ ]:


print('hello\nworld')
print('\thello')
print('        world')


# ### 1.4 Set `workspace` of the `env` object

# In[3]:


gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp


# ``` {admonition} Note:
#  🔔 `workspace` is an **attribute** of the `env` class in the `arcpy` package
#  ```

# In[5]:


getattr(arcpy.env, "workspace")


# In[6]:


type(arcpy.env)


# In[7]:


# view all attributes of the env class of ArcPy
print(dir(arcpy.env))


# ## 2. Basic Things to Know about ArcPy
# 
# ### 2.1 Naming Conventions of ArcPy functions
# 
# In ArcPy, a function is referenced by the geoprocessing (GP) **tool name** and
# the **alias of the toolbox** that the tool is contained.
# The first letter of every word in the tool name is capitalized.
# The alias of the toolbox are all in lowercase. 
# 
# - Old: `arcpy.<ToolName>_<toolboxalias>`
#   - Buffer: `arcpy.AddField_management`
#   - Add Field: `arcpy.AddField_management`
# - Modern: `arcpy.<toolboxalias>.<ToolName>`
#   - Buffer: `arcpy.analysis.Buffer`
#   - Add Field: `arcpy.management.AddField`
# 
# Following are the aliases for some commonly used toolbox.
# 
# | System Toolbox         | Alias        |
# |------------------------|--------------|
# | Analysis               | `analysis`   |
# | Conversion             | `conversion` |
# | Data Management        | `management` |
# | Editing                | `edit`       |
# | Geostatistical Analyst | `ga`         |
# | Network Analyst        | `na`         |
# | Spatial Analyst        | `sa`         |
# | Spatial Statistics     | `stats`      |

# ### 2.2 View the documentation of a function
# 
# 1. `Shift + Tab`
# 2. use the function's `.__doc__` attribute
# 3. `help(<function>)`
# 4. `? <function>`

# In[ ]:


arcpy.Buffer_analysis()


# In[2]:


print(arcpy.Buffer_analysis.__doc__)


# In[ ]:


help(arcpy.Buffer_analysis)


# In[ ]:


get_ipython().run_line_magic('pinfo', ' arcpy.Buffer_analysis')

