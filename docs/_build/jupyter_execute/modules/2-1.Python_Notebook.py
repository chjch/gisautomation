#!/usr/bin/env python
# coding: utf-8

# # 2-1: Jupyter Notebook

# ## What is Jupyter Notebook?
# 
# 1. An Integrated Development Environment (**IDE**) embedded in web browser. 
# 2. Experiment with your codes dynamicly (run your codes CELL BY CELL).
# 3. A light-weight application.
# 4. Powerful in sharing, visualizing, and presenting ideas and results of analysis.

# ## How to use Jupyter Notebook in ArcGIS Pro?
# - Start ArcGIS Pro -> Analysis (tab) -> Geoprocessing (group) -> Python Notebook.
# - Save the notebook. View and rename the notebook (\*.ipynb) in the **Catalog Pane**.
# - Run cells:
#     1. `Ctrl+Enter`: run a cell and stay focus on the current cell.
#     2. `Shift+Enter`: run a cell and move selection to the next cell.
#     3. `Alt+Enter`: run a cell and insert a new cell below the current cell.

# In[1]:


"Welcome to URP 6271"


# In[2]:


a = "today is saturday"


# ### Two modes
# 
# After a notebook is opened, it can be in either one of the two modes:
# 
# - **Command mode**: indicated by a <span style="color:blue">*blue*</span> vertical bar; press **Esc** key to enable. 
# - **Edit mode**: indicated by a <span style="color:green">*green*</span> vertical bar; press **Enter** to enable or simply click the cell.

# ### Two cell types
# 
# - **Code** cell: contains Python codes ready to run, indicated by `In [ ]`.
# - **Markdown** cell: contains markdown codes to complement the Python code, without `In [ ]`.

# In[3]:


"This is a code cell."


# This is a markdown cell.

# ### Useful shortcuts (only when in command mode)

# 1. `A`/`B`: Create a new cell above/below the current cell.
# 2. `UP`/`DOWN`: Arrow key to navigate between cells.
# 3. `M`: Convert a cell from code mode to markdown code.
# 4. `Y`: Convert a cell from markdown mode to code mode.
# 5. `D,D`: Delete a cell.
# 6. `L`: Toggle line number.
# 7. `F`: Find and replace text in markdown.
# 8. `H`: Show all keyboard shortcuts.

# ```{admonition} Tip:
# :class: tip
# Multi-cursor support in Jupyter Notebook
# 
# - Ctrl + mouse click
# - Alt + mouse click
# - [Helpful tricks in Jupyter Notebook](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
# 
# ```

# **<center>[Top 20](https://en.wikipedia.org/wiki/List_of_largest_cities) largest city in the world]</center>**
# 
# | Name           | Country        | Continent     | UN Estimation (2018) | Urban Area |
# |----------------|----------------|---------------|----------------------|------------|
# | Tokyo          |  Japan         | Asia          | 37,400,068           | 4,751      |
# | Delhi          |  India         | Asia          | 28,514,000           | 14,272     |
# | Shanghai       |  China         | Asia          | 25,582,000           | 5,436      |
# | Sao Paulo      |  Brazil        | South America | 21,650,000           | 6,949      |
# | Mexico City    |  Mexico        | South America | 21,581,000           | 9,017      |
# | Cairo          |  Egypt         | Africa        | 20,076,000           | 9,844      |
# | Mumbai         |  India         | Asia          | 19,980,000           | 22,010     |
# | Beijing        |  China         | Asia          | 19,618,000           | 4,659      |
# | Dhaka          |  Bangladesh    | Asia          | 19,578,000           | 36,928     |
# | Osaka          |  Japan         | Asia          | 19,281,000           | 5,129      |
# | New York       |  United States | North America | 18,819,000           | 684        |
# | Karachi        |  Pakistan      | Asia          | 15,400,000           | 14,648     |
# | Buenos Aires   |  Argentina     | South America | 14,967,000           | 5,033      |
# | Chongqing      |  China         | Asia          | 14,838,000           | 5,378      |
# | Istanbul       |  Turkey        | Europe        | 14,751,000           | 11,135     |
# | Kolkata        |  India         | Asia          | 14,681,000           | 13,830     |
# | Manila         |  Philippines   | Asia          | 13,482,000           | 12,798     |
# | Lagos          |  Nigeria       | Africa        | 13,463,000           | 7,877      |
# | Rio de Janeiro |  Brazil        | South America | 13,293,000           | 6,181      |
# | Tianjin        |  China         | Asia          | 13,215,000           | 3,886      |
