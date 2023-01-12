#!/usr/bin/env python
# coding: utf-8

# # 7-1: Raster Analysis Basics
# 
# ## 1. Raster Properties 
# 
# <img style="float: right;" src="https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/rasterbands.png">
# 
# ### 1.1 What is raster data?
# 
# In its simplest form, a raster consists of ***a matrix of cells*** (or pixels) organized into rows and columns (or a grid) where ***each cell contains a value*** representing information, such as temperature. Raster grids can be outputs from raseter analysis, digital aerial photographs, imagery from satellites, digital pictures, or even scanned maps.

# <!-- <div style="padding: 10px;margin-bottom: 20px;border: thin solid #FF7F27;border-left-width: 25px;background-color: #fff"><strong>Single-band: </strong> e.g., <i>temperature</i>, <i>elevation</i>, <i>soil pH value</i>.
# </div>
# 
# <img align="left" src="https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/raster_colormap.gif">
# <br> -->
# 
# ```{admonition} Single-band:
# Temperature, elevation, soil pH value
# ```
# ![ ](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/raster_colormap.gif)
# 

# <!-- <div style="padding: 10px;margin-bottom: 20px;border: thin solid #FF7F27;border-left-width: 25px;background-color: #fff"><strong>Multi-band and <a href="https://desktop.arcgis.com/en/arcmap/10.3/manage-data/raster-and-img/renderers-used-to-display-raster-data.htm#ESRI_SECTION2_6DA80CD25C02461BBD61A752F92D2E6D">RGB composite</a></strong> e.g., time series, satellite imagery.
# </div>
# 
# <img align="left" src="https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/rgb_composite.gif">
# <br> -->
# 
# ```{admonition} RGB composite:
# Time series, satellite imagery
# ```
# ![ ](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/rgb_composite.gif)
# 

#  <!-- <div style="padding: 10px;margin-bottom: 20px;border: thin solid #FF7F27;border-left-width: 25px;background-color: #fff"><strong>Comparison</strong>
# </div>
#  -->
# 
# |    single-band satellite image     |    3-band RGB composite satellite image    |
# |:----------------------------------:|:------------------------------------------:|
# | ![grayscale](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/grayscale.png) | ![rgb_composite](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/rgb_composite.png) |
# 

# ### 1.2 List Rasters

# In[1]:


import arcpy

gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp


# In[2]:


rasters = arcpy.ListRasters()
rasters


# ## 2. Run Raster Tools in ArcGIS Pro
# 
# ### 2.1 [Euclidean distance](https://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/euclidean-distance.htm)
# 
# ![ ](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/eucdist.gif)
# 
# ### 2.2 [Slice](https://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/slice.htm)
# 
# <!-- <div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff"><strong>Slice Method - Natural breaks:</strong> <a href="https://pro.arcgis.com/en/pro-app/help/mapping/layer-properties/data-classification-methods.htm#ESRI_SECTION1_B47C458CFF6A4EEC933A8C7612DA558B">Natural Breaks</a> classes are based on natural groupings inherent in the data.Class breaks are identified that best group similar values and that maximize the differences between classes. Natural breaks are data-specific classifications and not useful for comparing multiple maps built from different underlying information.
# </div> -->
# 
# ``` {admonition} Slice method- Natural Breaks:
# Natural Breaks classes are based on natural groupings inherent in the data.Class breaks are identified that best group similar values and that maximize the differences between classes. Natural breaks are data-specific classifications and not useful for comparing multiple maps built from different underlying information.
# ```
# 
# ![ ](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/slice.gif)
# ![ ](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/naturalbreaks.png)
# >

# ### 2.3 [Reclassify](https://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/reclassify.htm)
# - RemapValue
# - RemapRange

# ### 2.4. [Raster Calculator](https://pro.arcgis.com/en/pro-app/tool-reference/spatial-analyst/raster-calculator.htm)
# 
# - [Map Algebra Expression](https://pro.arcgis.com/en/pro-app/help/analysis/spatial-analyst/mapalgebra/working-with-operators.htm)

# ## 3. Raster Processing [Environment](https://pro.arcgis.com/en/pro-app/latest/tool-reference/environment-settings/an-overview-of-geoprocessing-environment-settings.htm)
# 
# General info about [Geoprocessing environment settings](https://pro.arcgis.com/en/pro-app/latest/tool-reference/environment-settings/what-is-a-geoprocessing-environment.htm).
# 
# "**MESC**" are the four most important environment settings for raster analysis.

# ```{admonition} Mask:
# set by feature class or data set
# ```
# 
# ![ ](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/mask.gif)

# ```{admonition} Extent:
# set by feature class, raster dataset, or coordinates of the sidees of the rectainge (Left, Right, Top, and Bottom).
# ```
# 
# ![ ](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/extent.png)

# ```{admonition} Snap raster:
# set by a raster dataset.
# ```
# 
# |            no snapping raster            |            with snapping raster                |
# |:----------------------------------------:|:----------------------------------------------:|
# | ![snap_left](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/snapRaster_left.png) | ![snap_right](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/snapRaster_right.png)     |

# <!-- <div style="padding: 10px;margin-bottom: 20px;border: thin solid #3F48CC;border-left-width: 25px;background-color: #fff"><strong><a href="https://pro.arcgis.com/en/pro-app/tool-reference/environment-settings/output-extent.htm">Cell size</a>:</strong> set by a raster dataset or number.
# </div> -->
# 
# ```{admonition} Cell size:
# set by a raster dataset or number.
# ```
# 
# ![ ](https://raw.githubusercontent.com/chjch/LAA6656/master/tutorials/img/cellSize.gif)
