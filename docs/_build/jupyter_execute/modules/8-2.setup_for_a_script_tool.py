#!/usr/bin/env python
# coding: utf-8

# # 8-2: Create a Script Tool 
# <img src="https://live.staticflickr.com/65535/51944863831_b009a5046f_o.png" width="473" height="492" alt="create_script" style="float:right">
# 
# ## 1. The setup process
# - Step 1. Pick a toolbox to host the tool
# - Step 2. Create a new script tool
# - Step 3. Setup the "General" tab
#     - Name: for operation (alphanumeric only and no spaces)
#     - Label: for display (all characters allowed)
#     - Link the .py script to the tool
# - Step 4. Setup the "Parameter" tab
#     - Name and label for each parameter
#     - Data Type: Feature Class, Field, String, Number (short, long, double), Boolean, and [other](https://desktop.arcgis.com/en/arcmap/10.3/tools/supplement/pdf/Geoprocessing_data_types.pdf)
#     - Type: Required or Optional
#     - Direction: Input (in most situation) or Output
# 
# [Official Document](https://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/setting-script-tool-parameters.htm#GUID-852D5C7F-B0EE-41A2-B6F8-1A86CD1DE3E7)

# <div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff">
#     
# _Step 3_
# 
# <img src="https://live.staticflickr.com/65535/51945181259_f8f27d4b2e_o.png" width="800" height="400" alt="wizard_general">
# 
# </div>

# <div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff">
#     
# _Step 4_
# 
# <img src="https://live.staticflickr.com/65535/51945473950_de9c5bffce_o.png" width="800" height="400" alt="wizard_parameter">
#     
# </div>

# #### Step 5. Modify the script (.py) to access values of parameters from the tool
# - ```arcpy.GetParameterAsText()```
# - access by position of the parameter, e.g., ```arcpy.GetParameterAsText(0)```

# In[1]:


# Define hard-coded parameter
I75_fc = "I75"
blkgrp_fc = "blockgroups"
cntbnd_fc = "county_boundary"
lawenforce_fc = "law_enforcement"


# In[2]:


# Access soft-coded parameter
I75 = arcpy.GetParameterAsText(1)
blkgrp = arcpy.GetParameterAsText(0)
cntbnd = arcpy.GetParameterAsText(2)
lawenforce = arcpy.GetParameterAsText(3)


# In[ ]:


output_gdb = arcpy.GetParameterAsText(4)
blkgrp_select = arcpy.GetParameterAsText(5)


# In[ ]:


# intermediate output
I75_buff = output_gdb + "\\" + "I75_Buff"
blkgrp_law = output_gdb + "\\" + "blkgrp_law"

