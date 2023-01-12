#!/usr/bin/env python
# coding: utf-8

# # 8-1: The Basics of a Script Tool

# <img src="https://live.staticflickr.com/65535/51945473980_8811fd9c3c_o.png" width="341" height="341" alt="script_tool" style="float: right">
# 
# ## 1. What is a script tool? 
# 
# A script tool allows you to turn your own **Python scripts** and functionality
# into your own **geoprocessing tools**.
# 
# - an integral part of geoprocessing, just like a system tool; 
# - open and run it in ArcGIS Pro;
# - use it in a ModelBuiler model.

# ## 2. What parts needed to create a script tool?
# 
# 1. The source code i.e., a Python script (.py).
# 2. A custom toolbox used to host script tools.
# 3. A precise definition of the parameters of your script (defined through a wizard in ArcGIS Pro).

# ## 3. Work on the script in Jupyter Notebook
# 
# <br>
# 
# <div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff">
# 
# **Homework 1 ModelBuilder model**: find census block groups without law enforcement.
# 
# <img src="https://gist.githubusercontent.com/chjch/6da40e9b15aef3a6571975f03ba90c93/raw/295f510ceada6f68dad90defe0b3ac1a9acdc6e2/hw1_mb.svg">
# 
# </div>

# In[1]:


# setup workspace
import arcpy
gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp


# In[2]:


# setup input feature classes
I75_fc = "I75"
blkgrp_fc = "blockgroups"
cntbnd_fc = "county_boundary"
lawenforce_fc = "law_enforcement"


# In[3]:


# setup output feature
output_gdb = r"..\data\class_data.gdb\module8\in class\FirstScriptTool\FirstScriptTool.gdb"
I75_buff = output_gdb + "\\" + "I75_Buff"
blkgrp_law = output_gdb + "\\" + "blkgrp_law"
blkgrp_select = "blockgroups_select"


# In[4]:


# geoprocessing operations 
arcpy.analysis.Buffer(I75_fc, I75_buff, "6 Miles")

blkgrp_lyr_1 = arcpy.management.SelectLayerByLocation(
    blkgrp_fc, "WITHIN", cntbnd_fc
)
blkgrp_lyr_2 = arcpy.management.SelectLayerByLocation(
    blkgrp_lyr_1, "WITHIN", I75_buff, selection_type="SUBSET_SELECTION"
)

arcpy.analysis.SpatialJoin(
    blkgrp_lyr_2, lawenforce_fc, blkgrp_law, 
    "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "INTERSECT", "", ""
)

query_exp = "{} = 0".format('"Join_Count"')
arcpy.FeatureClassToFeatureClass_conversion(
    blkgrp_law, output_gdb, blkgrp_select, query_exp, "", ""
)


# <div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff">
# 
# We now have the codes that does the job.
# Before making a "Script Tool", we need to put the codes in a python (**\*.py**) file.
