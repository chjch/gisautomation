#!/usr/bin/env python
# coding: utf-8

# # A Journey of Solving a GIS Automation Problem: from Google to Settle
# 

# ## 1. A Land Cover Map Created in ArcGIS

# <details>
#     <summary><u><b>ArcGIS Pro</b></u></summary>
# <img src="https://live.staticflickr.com/65535/51973472722_fca6427b9c_o.png" width="1512" height="998" alt="arcgis_landcover">
# </details>

# ## 2. Question: How to transfer the symbology to another software?

# <details>
#     <summary><u><b>QGIS</u></b></summary>
# <img src="https://live.staticflickr.com/65535/51974478781_4510e2f571_o.png" width="1512" height="999" alt="qgis_landcover">
# </details>

# ## 3. Let's ask Google.
# 
# ### 3.1 Google Search 1: "arcgis pro export symbology"
# 
# - https://community.esri.com/t5/arcgis-pro-ideas/arcgis-pro-quot-export-map-styles-quot-for-bulk/idi-p/937605
# - https://gis.stackexchange.com/questions/404262/how-to-save-symbol-to-style-for-layer-with-unique-values-style-in-arcgis-pro-2

# ### 3.2 Google Search 2: "save all symbols as a style arcgis pro"
# 
# - https://pro.arcgis.com/en/pro-app/2.7/help/mapping/layer-properties/save-symbols-in-styles.htm#:~:text=Click%20a%20symbol%20in%20the,open%20the%20Format%20Symbol%20pane.&text=in%20the%20upper%20right%20corner%20and%20click%20Save%20Symbol%20to%20Style.
# - https://gis.stackexchange.com/questions/404262/how-to-save-symbol-to-style-for-layer-with-unique-values-style-in-arcgis-pro-2

# ### 3.3 Google Search 3: "arcpy get rgb of symbology"
# 
# - https://community.esri.com/t5/python-questions/how-to-get-the-symbology-colors/td-p/475163

# ## 4. Solution: Access properties of symbology through `arcpy.mp` module
# 
# ### 4.1 Develop the code
# 
# - Think of the end goal: i.e., a pandas DataFrame containing all classes in a symbology with associated color rgb values.
# - What are the specific usage scenarios?
# - What tools are available? arcpy.mp, pandas
# - Establish a preliminary strategy (roadmap) to the final product.
# - Continue researching to figure out the nuts and bolts.
# 
# ### 4.2 Save for future use
# 
# - GitHub Gist
# - Let's talk about **git**.

# In[ ]:




