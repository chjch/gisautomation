#!/usr/bin/env python
# coding: utf-8

# # Introduction to ModelBuilder

# **Outline**:
# 
# - Feature classes in the class geodatabase
# - About this website (course materials)
# - A tour of ArcGIS Pro’s interface
#     - Maps and Scene,
#     - Contents and Catalog Pane
#     - Geoprocessing
#     - Tools and Toolboxes
# - Automation with ArcGIS ModelBuilder

# ## What is ModelBuilder
# 
# ArcGIS Pro [ModelBuilder](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/modelbuilder/what-is-modelbuilder-.htm) is a visual programming language for building _geoprocessing_ workflows.
# 
# - Build a model by [adding and connecting data and tools](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/modelbuilder/add-connect-and-modify-data-and-tools-in-a-model.htm)
# - [Iteratively](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/modelbuilder/iterators-for-looping.htm) process every feature class, raster, file, or table in a workspace.
# - Visualize your workflow sequence as an easy-to-understand diagram.
# - [Run a model](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/modelbuilder/run-a-model.htm) step-by-step, up to a selected step, or run the entire model.
# - [Make your model into a geoprocessing tool](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/modelbuilder/create-a-model-tool.htm) that can be shared or can be used in Python scripting and other models.

# ![mb-cenblk-select](../_static/images/mb_cenblk_select.png)

# ## Create a model
# 
# **Step 1**. Navigate to the _Toolboxes_ section in the _Catalog_ pane.
#    <br><img src="../_static/images/create_model.png" vspace="5px">

# **Step 2**. Modify the model's _Name_ and _Label_ by go to the _Properties_ menu.
#    <br><img src="../_static/images/mb_property.png" vspace="5px">
# 
# ```{note}
# 
# - Name only supports alphanumeric characters.
# - Label is what you see in ArcGIS Pro support all characters.
# ```

# **Step 3**. Start to design the model's workflow by adding data and geoprocessing functions.

# ## Problem 1

# ```{admonition} Question:
# :class: tip
# Find census blockgroups that have at least one school within 2 miles of I-75
# 
# <details>
#   <summary><strong>Solution</strong></summary>
# 
#   - Create a 2-mile buffer around I-75 (Buffer)
#   - Use this buffer to clip schools (Clip)
#   - Spatial Join the schools to blockgroups (Spatial Join)
#   - Select blockgroups that have at least one school (select by Location)
#   - Save the selected features as a separate layer (Copy Features)
#   
# </details>
# ```

# ## Problem 2

# ```{admonition} Question:
# :class: tip
# Develop an index as a ratio of street length to the blockgroup area
# 
# <details>
#   <summary><strong>Solution</strong></summary>
# 
#   - Intersect roads by blockgroups (Intersect)
#   - Spatial Join roads to blockgroups (Spatial Join)
#     - Choose to Sum the length of the roads during spatial join 
#   - Add and calculate a new field as the ratio of total road lengths by blockgroups area  (Calculate Field)
#   
# </details>
# ```

# 
