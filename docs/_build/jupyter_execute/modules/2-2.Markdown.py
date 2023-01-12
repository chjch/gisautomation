#!/usr/bin/env python
# coding: utf-8

# # 2-2: Markdown

# ![markdown-mark](../_static/images/Markdown-mark.svg)
# 
# Markdown is a _lightweight_ **markup language** for creating formatted text using a
# plain-text editor.
# 
# Jupyter notebook has built-in support for the Markdown language.
# 
# Besides staying inside a notebook file (.ipynb), markdown codes can also exists in
# its own file (more commonly) with an file extension (\*.md).

# ## 1. Basic Syntax of Markdown

# 1. Header
#     - `# H1`
#     - `## H2`
# 2. Emphasize
#     - Italic: `_`
#     - Bold: `**`
#     - Italic and Bold
# 3. List
#     - Unordered list: `*`, `-`, `+`
#     - Ordered list: `1.`, `2.`, `3.`
#     - Nested list
#     - To do list
# 4. Link 
#     - Website: `[name of link](url)`, e.g., `[Markdown Cheatsheet](https://en.support.wordpress.com/markdown-quick-reference/)`
#     - Image: `![alttext](path to image)`

# ## 2. An Example

# ```{admonition} Markdown
# 
# <details>
#   <summary><strong>Show Raw Text</strong></summary>
# 
#   [link](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/a-quick-tour-of-arcpy.htm)
#   A quick tour of ArcPy
#   ArcPy is a Python site package that provides a useful and productive way to perform geographic data analysis, data conversion, data management, and map automation with Python.
#   Running a tool
#   arcpy.Buffer_analysis("c:/data/Portland.gdb/streets", "c:/data/Portland.gdb/steets_buffer", "500 METERS")
#   Working with modules
#   ArcPy includes modules covering other areas of ArcGIS. ArcPy is supported by a series of modules, including the following:
#   Charts module (arcpy.charts)
#   Data Access module (arcpy.da)
#   Geocoding module (arcpy.geocoding)
#   Image Analysis module (arcpy.ia)
#   Mapping module (arcpy.mp)
#   Metadata module (arcpy.metadata)
#   Network Analyst modules (arcpy.nax and arcpy.na)
#   Sharing module (arcpy.sharing)
#   Spatial Analyst module (arcpy.sa)
#   Workflow Manager (Classic) module (arcpy.wmx)
#   Related topics
#   What is ArcPy?
#   Essential ArcPy vocabulary
#   Install ArcPy
#   Importing ArcPy
#   
# </details>
# ```
# 
# 

# # A quick tour of ArcPy
# 
# ArcPy is a Python site package that provides a useful and productive way to perform geographic data analysis, data conversion, data management, and map automation with Python.
# 
# ## Running a tool
# 
# `arcpy.Buffer_analysis("c:/data/Portland.gdb/streets", "c:/data/Portland.gdb/steets_buffer", "500 METERS")`
# 
# ## Working with modules
# ArcPy includes modules covering other areas of ArcGIS. ArcPy is supported by a series of modules, including the following:
# 
# - Charts module (**arcpy.charts**)
# - Data Access module (**arcpy.da**)
# - Geocoding module (**arcpy.geocoding**)
# - Image Analysis module (**arcpy.ia**)
# - Mapping module (**arcpy.mp**)
# - Metadata module (**arcpy.metadata**)
# - Network Analyst modules (**arcpy.nax** and **arcpy.na**)
# - Sharing module (**arcpy.sharing**)
# - Spatial Analyst module (**arcpy.sa**)
# - Workflow Manager (Classic) module (**arcpy.wmx**)
# 
# ## Related topics
# - [What is ArcPy?](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm)
# - [Essential ArcPy vocabulary](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/essential-arcpy-vocabulary.htm)
# - [Install ArcPy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/installing-arcpy.htm)
# - [Importing ArcPy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/importing-arcpy.htm)
# 
# 
# 

# ## 3. Support of LaTeX

# **What is LaTeX**
# 
# - [LaTeX](https://www.latex-project.org/) is a software system for document preparation.
#   When writing, the writer uses plain text as opposed to the formatted text found in
#   "What You See Is What You Get" word processors, such as _Microsoft Word_.
# - LaTeX started as a writing tool for mathematicians and computer scientists, but even
#   from early in its development, it has also been taken up by scholars who needed to
#   write documents that include **complex math expressions**.

# Jupyter Notebook has built-in support for LaTeX, which makes it even more appealing
# for presentation and instruction purposes.
# When writing equation in LaTeX, simply enclose the equation with `$`.

# ```{admonition} Note
# To work with LaTeX in Jupyter, the cell must be a **markdown** cell.
# ```

# As an example, let's write some euqation on the
# [ArcGIS Documentation](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/h-how-average-nearest-neighbor-distance-spatial-st.htm).

# $$SE=\frac{0.26136}{\sqrt{n^2/A}}$$
