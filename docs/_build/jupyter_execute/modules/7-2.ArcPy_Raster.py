#!/usr/bin/env python
# coding: utf-8

# # 7-2: Run Raster Geoprocessing using ArcPy
# 
# ## 1. Setup "mesc" for ArcPy

# In[1]:


import arcpy

gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp


# ### 1.1 `env` object
# 
# The [env](https://pro.arcgis.com/en/pro-app/arcpy/classes/env.htm) object exposes
# **environment settings** for geoprocessing functions in ArcGIS.
# 
# These properties can be used to retrieve (_read_) the current values or to set
# (_write_) them.
# 
# Geoprocessing environment settings can be thought of as **additional parameters**
# that affect a tool's results.
# 
# ### 1.2 Set mask

# In[2]:


arcpy.env.mask = "county_boundary"  # set mask by a feature class


# In[3]:


arcpy.env.mask = "dem"  # set mask by a raster dataset


# ### 1.3 Set extent and Read extent

# In[4]:


arcpy.env.extent = "county_boundary" # set extent by a feature class


# In[6]:


arcpy.env.extent = "dem"


# In[10]:


# read the left, right, top, bottom coordinates of the extent setting
extent_info = "Left:\t{}\nRight:\t{}\nTop:\t{}\nBottom:\t{}".format(
    arcpy.env.extent.XMin, 
    arcpy.env.extent.XMax, 
    arcpy.env.extent.YMax, 
    arcpy.env.extent.YMin
)


# In[ ]:


print(extent_info)


# ### 1.4 Set snap raster

# In[11]:


arcpy.env.snapRaster = "dem" # can only be set by a raster dataset


# ### 1.5 Set cell size

# In[12]:


arcpy.env.cellSize = "dem" # set output raster cell size by another raster


# In[13]:


arcpy.env.cellSize = 90 # set output raster cell size by a number (in default linear unit)


# ## 2. Run Raster Functions using ArcPy

# In[14]:


# setup "mesc"

cntbnd_fc = "county_boundary"
dem_rast = "dem"

arcpy.env.mask = cntbnd_fc
arcpy.env.extent = cntbnd_fc
arcpy.env.snapRaster = None
arcpy.env.cellSize = 30


# ### 2.1 Setup output geodatabse

# In[5]:


import os

output_gdb = r"..\data\class_data.gdb\module7\in class\Raster\Raster.gdb"
os.path.join(output_gdb, 'out_rast') # with built-in function


# In[6]:


output_gdb + "\\" + 'out_rast' # with string concatnation


# In[7]:


"{}\{}".format(output_gdb, 'out_rast') # with .format function


# ### 2.2 Euclidean Distance

# In[15]:


get_ipython().run_line_magic('pinfo', 'arcpy.sa.EucDistance')


# In[21]:


school_fc = "schools"

school_dist_rast = arcpy.sa.EucDistance(school_fc)   # cell_size using default setup in env parameter
school_dist_rast.save(os.path.join(output_gdb, 'school_dist_rast'))


# ### 2.3 Slice

# In[20]:


get_ipython().run_line_magic('pinfo', 'arcpy.sa.Slice')


# In[22]:


arcpy.env.snapRaster = school_dist_rast

school_dist_1_9 = arcpy.sa.Slice(
    school_dist_grid,
    number_zones=9, 
    slice_type="NATURAL_BREAKS",
    base_output_zone=1
)

school_dist_1_9.save(output_gdb + "\\" + "school_dist_1_9")


# ### 2.4 Reclassify
# 
# - [_RemapValue_](https://pro.arcgis.com/en/pro-app/arcpy/spatial-analyst/remapvalue-class.htm) object takes **a list of lists**, with the inner lists being composed of 2 parts
#     + oldValue
#     + newValue
# - [_RemapRange_](https://pro.arcgis.com/en/pro-app/arcpy/spatial-analyst/an-overview-of-transformation-classes.htm) object takes **a list of lists**, with the inner lists being composed of 3 parts
#     + startValue
#     + endValue
#     + newvalue

# In[27]:


get_ipython().run_line_magic('pinfo', 'arcpy.sa.Reclassify')


# In[23]:


dist_remap = arcpy.sa.RemapValue(
    [[1, 9], [2, 8], [3, 7], [4, 6],
     [6, 4], [7, 3], [8, 2], [9, 1]]
)

school_dist_9_1 = arcpy.sa.Reclassify(school_dist_1_9, "Value", dist_remap)
school_dist_9_1.save("{}\{}".format(output_gdb, "school_dist_9_1"))


# ### 2.5 Map Algebra directly operated on rasters

# In[25]:


school_dist_wgted = school_dist_9_1*0.3 + school_dist_1_9*0.7
school_dist_wgted.save(os.path.join(output_gdb, "school_dist_wgted"))


# In[29]:


get_ipython().run_line_magic('pinfo', 'arcpy.sa.Int')


# In[26]:


# without defining a variable to store the output raster

arcpy.sa.Int(school_dist_wgted).save(
    os.path.join(output_gdb, "school_dist_wgted_int")
)

