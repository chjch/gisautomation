#!/usr/bin/env python
# coding: utf-8

# # 8-3:  Add Additional Features to the Script Tool
# 
# ## 1. Add Message to the running window
# 
# - ```arcpy.AddMessage()```

# In[1]:


# setup workspace
import arcpy
gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp

# setup input feature classes
# Access soft-coded parameter
I75 = arcpy.GetParameterAsText(1)
blkgrp = arcpy.GetParameterAsText(0)
cntbnd = arcpy.GetParameterAsText(2)
lawenforce = arcpy.GetParameterAsText(3)

# setup output feature
output_gdb = arcpy.GetParameterAsText(4)
blkgrp_select = arcpy.GetParameterAsText(5)
I75_buff = output_gdb + "\\" + "I75_Buff"
blkgrp_law = output_gdb + "\\" + "blkgrp_law"

# geoprocessing operations 
arcpy.Buffer_analysis(I75, I75_buff, "6 Miles")
arcpy.AddMessage("Finished buffer {}".format(I75))

blkgrp_lyr_1 = arcpy.SelectLayerByLocation_management(
    blkgrp, "WITHIN", cntbnd
)
blkgrp_lyr_2 = arcpy.SelectLayerByLocation_management(
    blkgrp_lyr_1, "WITHIN", I75_buff
)
arcpy.AddMessage("Finished Select by location.")

arcpy.SpatialJoin_analysis(
    blkgrp_lyr_2, lawenforce, blkgrp_law, 
    "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "INTERSECT", "", ""
)
arcpy.AddMessage("Finished creating {}".format(blkgrp_law))

query_exp = "{} = 0".format('"Join_Count"')
arcpy.FeatureClassToFeatureClass_conversion(
    blkgrp_law, output_gdb, blkgrp_select, query_exp, "", ""
)
arcpy.AddMessage("All tasks are completed.")


# ## 2. Add Progress bar
# - Useful when tasks taking very long.
# - A time-consuming loop presented in the script.
# - ```arcpy.SetProgressor()```
#     + type
#         * default
#         * step
#     + min_range
#     + max_range
#     + step_value
# - ```arcpy.SetProgressorPosition()```
# - ```arcpy.ResetProgressor()```
# - [Official Document](https://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/understanding-the-progress-dialog-in-script-tools.htm)

# In[ ]:


import arcpy
gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp

# setup input feature classes
# Access soft-coded parameter
I75 = arcpy.GetParameterAsText(1)
blkgrp = arcpy.GetParameterAsText(0)
cntbnd = arcpy.GetParameterAsText(2)
lawenforce = arcpy.GetParameterAsText(3)

# setup output feature
output_gdb = arcpy.GetParameterAsText(4)
blkgrp_select = arcpy.GetParameterAsText(5)
I75_buff = output_gdb + "\\" + "I75_Buff"
blkgrp_law = output_gdb + "\\" + "blkgrp_law"

# geoprocessing operations 
arcpy.SetProgressor("step", "tool running", 0, 5, 1)
arcpy.Buffer_analysis(I75, I75_buff, "6 Miles")
arcpy.AddMessage("Finished buffer {}".format(I75))
arcpy.SetProgressorPosition()

blkgrp_lyr_1 = arcpy.SelectLayerByLocation_management(
    blkgrp, "WITHIN", cntbnd
)
arcpy.SetProgressorPosition()
blkgrp_lyr_2 = arcpy.SelectLayerByLocation_management(
    blkgrp_lyr_1, "WITHIN", I75_buff
)
arcpy.SetProgressorPosition()
arcpy.AddMessage("Finished Select by location.")

arcpy.SpatialJoin_analysis(
    blkgrp_lyr_2, lawenforce, blkgrp_law, 
    "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "INTERSECT", "", ""
)
arcpy.AddMessage("Finished creating {}".format(blkgrp_law))
arcpy.SetProgressorPosition()

query_exp = "{} = 0".format('"Join_Count"')
arcpy.FeatureClassToFeatureClass_conversion(
    blkgrp_law, output_gdb, blkgrp_select, query_exp, "", ""
)
arcpy.AddMessage("All tasks are completed.")
arcpy.SetProgressorPosition()
arcpy.ResetProgressor()


# ## 3. Add Overwrite Checkbox
# - Parameter Setting
#     + Data Type: Boolean
#     + Type: Optional
#     + Default: False
# - ```arcpy.GetParameter()```

# In[ ]:


import arcpy
gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp

# setup input feature classes
# Access soft-coded parameter
I75 = arcpy.GetParameterAsText(1)
blkgrp = arcpy.GetParameterAsText(0)
cntbnd = arcpy.GetParameterAsText(2)
lawenforce = arcpy.GetParameterAsText(3)

# setup output feature
output_gdb = arcpy.GetParameterAsText(4)
blkgrp_select = arcpy.GetParameterAsText(5)
I75_buff = output_gdb + "\\" + "I75_Buff"
blkgrp_law = output_gdb + "\\" + "blkgrp_law"

ow = arcpy.GetParameter(6)
if ow is True:
    arcpy.env.overwriteOutput = True
arcpy.AddMessage(str(ow))

# geoprocessing operations 
arcpy.SetProgressor("step", "tool running", 0, 5, 1)
arcpy.Buffer_analysis(I75, I75_buff, "6 Miles")
arcpy.AddMessage("Finished buffer {}".format(I75))
arcpy.SetProgressorPosition()

blkgrp_lyr_1 = arcpy.SelectLayerByLocation_management(
    blkgrp, "WITHIN", cntbnd
)
arcpy.SetProgressorPosition()
blkgrp_lyr_2 = arcpy.SelectLayerByLocation_management(
    blkgrp_lyr_1, "WITHIN", I75_buff
)
arcpy.SetProgressorPosition()
arcpy.AddMessage("Finished Select by location.")

arcpy.SpatialJoin_analysis(
    blkgrp_lyr_2, lawenforce, blkgrp_law, 
    "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "INTERSECT", "", ""
)
arcpy.AddMessage("Finished creating {}".format(blkgrp_law))
arcpy.SetProgressorPosition()

query_exp = "{} = 0".format('"Join_Count"')
arcpy.FeatureClassToFeatureClass_conversion(
    blkgrp_law, output_gdb, blkgrp_select, query_exp, "", ""
)
arcpy.AddMessage("All tasks are completed.")
arcpy.SetProgressorPosition()
arcpy.ResetProgressor()


# ## 4. Useful resource
# 
# - [A quick tour of creating tools with Python](https://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/a-quick-tour-of-creating-tools-in-python.htm)
# - [Comparing custom and Python toolboxes](https://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/comparing-custom-and-python-toolboxes.htm)
# - [Creating script tools in a custom toolbox](https://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/adding-a-script-tool.htm)
# - [Customizing script tool behavor](https://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/customizing-script-tool-behavior.htm)
# - [Programming a ToolValidator class](https://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/programming-a-toolvalidator-class.htm)
