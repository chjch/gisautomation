#!/usr/bin/env python
# coding: utf-8

# # 6-2: Visualizing Spatial Data using ArcGIS API for Python
# 
# ## 1. Introduction to the ArcGIS API for Python
# 
# - The ArcGIS API for Python, i.e., the `arcgis` package, is a powerful, modern and easy to use Pythonic library to perform GIS **visualization** and analysis, spatial data management and GIS system administration tasks that can run both in an interactive fashion, as well as using scripts.
# - Shipped with the ArcGIS Pro installation file
# 
# Helpful resource on **arcgis**:
# - [An overview of the API](https://developers.arcgis.com/python/guide/overview-of-the-arcgis-api-for-python/)
# - [GitHub: ArcGIS API for Python](https://github.com/Esri/arcgis-python-api)

# In[1]:


get_ipython().run_cell_magic('html', '', '<iframe width="560" height="315" src="https://www.youtube.com/embed/irpubkYLrWI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n')


# ### 1.1 Import the package

# In[2]:


import arcgis


# In[3]:


from arcgis import GIS, GeoAccessor, GeoSeriesAccessor, pd


# ### 1.2 The _GIS_ class from the _gis_ module
# 
# - what is **class** in Python?
#     + it is a blueprint for building things (a machine produces products)
#     + things get created from the class are called objects (or instances of the class)
#     + DRY (Don't repeat yourself) code. 
#     + example:
#         * a college student
#         * a data structure that organizes the data -- _NumPy_ array and _pandas_ DataFrame
# - what is **gis** (Geographic Information System)?
#     + Geographic Data:
#         * collection
#         * storage
#         * manipulation
#         * analysis
#         * visualization
#         * management/administration
#         * distribution
#     + A variety of technologies:
#         * human activities (such as conducting survey of a area of land)
#         * hardware
#         * software (a narrower definition of GIS)
# - The **GIS** class
#     + from the **gis** module (the core) of the _arcgis_ package 
#     + a portal to do GIS
#     + can link to an ArcGIS Online account
#     + or, be used locally without the connection

# ## 2. Spatially Enabled DataFrame (SEDF)
# 
# ### 2.1 What is SEDF
# 
# - A class from the _features_ module of _arcgis_ (`arcgis.features`)
#     + contains types and functions for working with features and feature layers in the GIS.
# - An extension of the `DataFrame` class from _pandas_
# - we use ArcPy as the geometry engine for this module, which gives us access to all native GIS data ArcGIS Pro supports

# ### 2.2 Load a feature class as SEDF

# In[4]:


from arcgis import pd, GeoAccessor, GeoSeriesAccessor
import arcpy

gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp
blkgrp_fc = "blockgroups"


# In[5]:


blkgrp_sedf = pd.DataFrame.spatial.from_featureclass(blkgrp_fc)
blkgrp_sedf.head()


# In[5]:


len(blkgrp_sedf)  # recall


# In[6]:


blkgrp_sedf.shape  # recall


# In[7]:


blkgrp_sedf['TOTALPOP'].values


# ## 3. Visualizing GIS data
# 
# ### 3.1 Create a map
# 
# 1. **<font color='royalblue'>Import all the necessary modules</font>**

# In[8]:


from arcgis import GIS, GeoAccessor, GeoSeriesAccessor, pd


# 2. **<font color='royalblue'>Create a `GIS` instance</font>**

# In[9]:


my_gis = GIS()


# In[10]:


my_gis


# 3. **<font color='royalblue'>Load data in the "GIS" as SEDF</font>**

# In[11]:


import arcpy
gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp

blkgrp = "blockgroups"
schools = 'schools'


# In[12]:


blkgrp_sedf = pd.DataFrame.spatial.from_featureclass(blkgrp)
schools_sedf = pd.DataFrame.spatial.from_featureclass(schools)


# 4. **<font color='royalblue'>Use the map widget from the `GIS` instance to create a map</font>**

# In[13]:


# call the map() function from the GIS instance
my_map_in_my_gis = my_gis.map(location=[29.7, -82.3], zoomlevel=9)


# In[14]:


my_map_in_my_gis


# 5. **<font color='royalblue'>Load SEDFs into the map</font>**
# 
# - call `spatial.plot()` from the sedf
# - last loaded sedf will be displayed on the top

# In[15]:


blkgrp_sedf.spatial.plot(map_widget=my_map_in_my_gis)


# In[16]:


schools_sedf.spatial.plot(map_widget=my_map_in_my_gis,
                          col='NAME', 
                          renderer_type='u')


# ### 3.2 Modify the size of the widget window

# In[17]:


from ipywidgets import Layout


# In[18]:


my_map_in_my_gis.layout = Layout(height="600px")


# In[19]:


my_map_in_my_gis.layout = Layout(width="600px", height="600px")


# In[20]:


my_map_in_my_gis


# ### 3.3 Change the Basemap
# 
# 1. `basemaps` attribute of a `map` returns a list of available basemaps

# In[21]:


my_map_in_my_gis.basemaps


# In[22]:


my_map_in_my_gis


# 2. Set basemap by assign a value in the list to the `basemap` attribut.

# In[23]:


my_map_in_my_gis.basemap = 'dark-gray'


# ### 3.4 Choropleth Map

# In[24]:


from arcgis import mapping


# In[25]:


mapping.display_colormaps()


# In[26]:


map2 = my_gis.map(location=[29.7, -82.3], zoomlevel=10)


# In[27]:


blkgrp_sedf.spatial.plot(map_widget=map2, colors="YlGnBu",
                         col='TOTALPOP', renderer_type='c',
                         method='esriClassifyNaturalBreaks',
                         class_count=7)


# In[28]:


from ipywidgets import Layout
map2.layout = Layout(height="700px")


# In[29]:


map2

