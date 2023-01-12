#!/usr/bin/env python
# coding: utf-8

# # 6-1: Visualize tabular (aspatial) data using Matplotlib
# 
# - Matplotlib is the most popular plotting library
# - Works with NumPy and pandas DataFrame
# - Allow you to tweak every single detail of your plot. 
# - Similar experience to MatLab's graphical plotting.
#     
# Helpful resource on **Matplotlib**:
# - [Matplotlib official website - Gallery](https://matplotlib.org/gallery/index.html)
# - [Matplotlib playlist from Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_)
# 
# ## 1. Setup and Import All Modules

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # yet another convention


# Recall how we convert feature class to numpy array to pandas DataFrame.

# In[2]:


import arcpy

gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp
blkgrp_fc = "blockgroups"


# In[3]:


def fc_to_df(fc):
    fields = [field.name for field in arcpy.ListFields(fc)]
    arr = arcpy.da.FeatureClassToNumPyArray(fc, fields[2:])
    return pd.DataFrame(arr, columns=fields[2:])


# In[4]:


blkgrp_df = fc_to_df(blkgrp_fc)
blkgrp_df.head()


# ## 2. Setup a plot: Figure and axis
# 
# ```{admonition} ⚠️ WARNING:
# Python Notebook in ArcGIS Pro currently does not support plotting.
# To use matplotlib and view the plots, you must open the jupyter notebook from browser.
# ```

# In[5]:


fig, axis = plt.subplots()


# In[6]:


fig, axis = plt.subplots(nrows=2, ncols=2)


# ## 3. Create plots with attribute data

# In[7]:


blkgrp_df.columns.values


# ### 3.1 A simple scatter plot

# In[8]:


fig, axis = plt.subplots()
axis.scatter(blkgrp_df["TOTALPOP"], blkgrp_df["HOUSEHOLDS"])


# ### 3.2 Change figure size
# 
# - the figure size argument: `figsize`
# - supply as a tuple `(width, height)`

# In[9]:


fig, axis = plt.subplots(figsize=(10,8))
axis.scatter(blkgrp_df["TOTALPOP"], blkgrp_df["HOUSEHOLDS"])


# ### 3.3 Add labels and title
# 
# - `set_xlabel()`
# - `set_ylabel()`
# - `set_title()`

# In[10]:


fig, axis = plt.subplots(figsize=(10, 8))
axis.scatter(blkgrp_df["TOTALPOP"], blkgrp_df["HOUSEHOLDS"])
axis.set_xlabel("total population")
axis.set_ylabel("number of households")
axis.set_title("2010 Alachua County Census Block Group")


# ### 3.4 Change color and marker
# 
# Set the ```color``` argument or ```c```
# 
# ![base color](https://matplotlib.org/stable/_images/sphx_glr_named_colors_001.png)
# ![tableau color](https://matplotlib.org/stable/_images/sphx_glr_named_colors_002.png)
# ![css color](https://matplotlib.org/stable/_images/sphx_glr_named_colors_003.png)

# In[11]:


fig, axis = plt.subplots(figsize=(10,6))
axis.scatter(blkgrp_df["TOTALPOP"], blkgrp_df["HOUSEHOLDS"], color="tab:orange")


# Set the ```marker``` argument or ```m```
# 
# [Matplotlib markers](https://matplotlib.org/stable/api/markers_api.html)

# In[12]:


fig, axis = plt.subplots(figsize=(10,6))
axis.scatter(blkgrp_df["TOTALPOP"], blkgrp_df["HOUSEHOLDS"], color="darkgreen", marker='s')


# Set the size of the marker `s`

# In[13]:


fig, axis = plt.subplots(figsize=(10,6))
axis.scatter(blkgrp_df["PCT_POV"], blkgrp_df["MEDHHINC"], 
             color="purple", s=blkgrp_df['TOTALPOP']/100)


# ### 3.5 A bar plot
# 
# - use `bar()` to plot 
# - the `width` argument

# In[14]:


fig, axis = plt.subplots()   # tuple unpacking
axis.bar(np.arange(10), blkgrp_df["FEMALE"][:10], 
         width=0.3, color="tab:blue")
axis.bar(np.arange(10), blkgrp_df["MALE"][:10], 
         width=0.3, color="tab:orange")


# In[15]:


fig, axis = plt.subplots()   # tuple unpacking
axis.bar(np.arange(10)-0.15, blkgrp_df["FEMALE"][:10], 
         width=0.3, color="tab:blue")
axis.bar(np.arange(10)+0.15, blkgrp_df["MALE"][:10], 
         width=0.3, color="tab:orange")


# ### 3.6 Add legend 
# 
# - set the `label` argument
# - use the `.legend()` function

# In[16]:


fig, axis = plt.subplots()   # tuple unpacking
axis.bar(np.arange(10)-0.15, blkgrp_df["FEMALE"][:10], 
         width=0.3, color="tab:blue", label="WOMAN")
axis.bar(np.arange(10)+0.15, blkgrp_df["MALE"][:10], 
         width=0.3, color="tab:orange", label="MAN")
axis.legend()


# In[17]:


fig, axis = plt.subplots(figsize=(12,6))   # tuple unpacking
axis.bar(np.arange(20)-0.15, blkgrp_df["WHITE"][:20], 
         width=0.3, color="tab:blue", label="WHITE")
axis.bar(np.arange(20)+0.15, blkgrp_df["BLACK"][:20], 
         width=0.3, color="tab:orange", label="BLACK")
axis.legend(loc=1)


# ### 3.7 Create a histogram
# - use the `hist()` to plot
# - set the `bin()` argument

# In[18]:


fig, axis = plt.subplots()
axis.hist(blkgrp_df["TOTALPOP"])


# In[19]:


fig, axis = plt.subplots()
axis.hist(blkgrp_df["TOTALPOP"], bins=15)


# In[20]:


fig, axis = plt.subplots()
axis.hist(blkgrp_df["TOTALPOP"], bins=15, color="purple")


# In[21]:


fig, axis = plt.subplots()
axis.hist(blkgrp_df["TOTALPOP"], bins=15, color="teal", orientation="horizontal")


# In[22]:


fig, axis = plt.subplots()
axis.hist(blkgrp_df["TOTALPOP"], bins=15, color="red", histtype="step")


# ### 3.8 Display two plots side by side
# 
# Each axis is an element of the axes list.

# In[23]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,6))
axes[0].hist(blkgrp_df["TRAN_BIKE"], color="purple")
axes[1].hist(blkgrp_df["TRAN_CAR"], color="teal")


# In[24]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,6))
axes[0].hist(blkgrp_df["TRAN_CAR"], bins=15, color="purple")
axes[1].hist(blkgrp_df["TRAN_BIKE"], bins=15, color="teal")
plt.tight_layout()

