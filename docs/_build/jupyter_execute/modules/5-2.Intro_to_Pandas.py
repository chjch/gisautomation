#!/usr/bin/env python
# coding: utf-8

# # 5-2: Using Pandas for ArcGIS
# 
# - pandas is built on top of NumPy
# - the "_excel sheet_" of Python
# - fast data analysis that improves your productivity
# 
# **Helpful resource on pandas:**
# - [pandas official website - Getting started](https://pandas.pydata.org/docs/getting_started/index.html)
# - [pandas playlist from Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS)

# ## 1. Import the pandas package

# In[1]:


import numpy as np
import pandas as pd # this is also a convention 


# ## 2. Series object
# 
# [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) is the fundamental data structure of the pandas package.
# 
# A `pandas.Series` object is an 1-dimensional ndarray.
# 
# The key difference comparing with a numpy array is that Series have **indexed labels**.
# 
# ### 2.1 Create a pandas Series

# In[2]:


my_list = list(range(10))
my_list


# In[3]:


pd.Series(my_list) # note that the S in Series is upper case


# In[4]:


import string
string.ascii_lowercase[:10]


# In[5]:


labels = list(string.ascii_lowercase[:10])
labels


# ### 2.2 Series with label index
# 
# Check the documentation for arguments

# In[6]:


pd.Series(data=my_list, index=labels)  # named argument or keyword argument


# In[7]:


pd.Series(my_list, labels)  # positional argument


# In[8]:


my_sr = pd.Series(my_list, labels)


# ### 2.3 indexing and slicing for Series
# 
# - indexing by label
# - indexing by location

# In[9]:


my_sr['c']   # indexing by label


# In[10]:


my_sr[2]   # indexing by position


# In[11]:


my_sr[2:8]


# ### 2.4 Operations on Series
# 
# ``` {admonition} Note:
# Pandas perform operations based on labels (indicies)
# ```
# 
# <font color='steelblue'>**Top 3 U.S. State by Population**</font>
# 
# State|Population
# --|----------
# CA|39512223
# TA|28995881
# FL|21477737

# <font color='steelblue'>**Top 3 U.S. State by Area**</font>
# 
# State|Area(sq mi)
# --|----------
# AL|665384
# TA|268596	
# CA|163694

# In[12]:


"CA TA FL".split(" ")  # use split() function of string to split on space 


# In[13]:


"CA TA FL".split() # split() acts on space by default


# In[14]:


sr1 = pd.Series(data=[39512223, 28995881, 21477737],
                index="CA TA FL".split())
sr1


# In[15]:


round(sr1 / 1000000, 2)


# In[16]:


"AL,TA,CA".split(",")


# In[17]:


sr2 = pd.Series([665384, 268596, 163694], "AL,TA,CA".split(","))
sr2


# In[18]:


sr1 / sr2


# ## 3. DataFrame object
# 
# [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html): **Two-dimensional** (rows & columns), size-mutable, potentially heterogeneous tabular data.
# 
# `DataFrame` consists of one or more `Series` that shares the same labels (indicies).
# 
# It is the **DataFrame** structure makes pandas a powerful tool for scientific data analysis.
# 
# ### 3.1 Create DataFrame from Series

# In[19]:


pd.DataFrame(sr1, columns=['population']) # note that the column names must be supplied as a list


# `concat` function: series are supplied as **a list**

# In[20]:


pd.concat([sr1, sr2], axis=1) # axis=1 means on columns


# In[21]:


pd.concat([sr1, sr2]) # by default, axis=0, meaning on rows


# `concat` function: series are supplied as **a dictionary**

# In[22]:


pd.concat({'population': sr1, 'area (sq mi)': sr2}, axis=1)


# ### 3.2 Convert numpy Structured Array to pandas DataFrame
# 
# Recall how we convert a feature class to a **structured ndarray**

# In[23]:


import arcpy

gdb_worksp = r"..\data\class_data.gdb"
arcpy.env.workspace = gdb_worksp
school_fc = "schools"

school_arr = arcpy.da.FeatureClassToNumPyArray(school_fc, '*') # use '*' to get all fields


# In[41]:


school_arr.dtype.names


# In[42]:


columns = ["NAME", 'OP_CLASS', 'ENROLLMENT', 'TYPE', 'TEACHERS']
school_arr = arcpy.da.FeatureClassToNumPyArray(school_fc, columns)

pd.DataFrame(school_arr, columns=columns) # first columns and second columns


# ### 3.3 preview the head and tail of a DataFrame

# In[43]:


school_df = pd.DataFrame(school_arr, columns=columns)
school_df.head()


# In[44]:


school_df.tail()


# In[45]:


school_df.head(10)


# ### 3.4 Indexing and Slicing
# 
# Select single column return a pandas **Series**

# In[46]:


school_df["NAME"]


# Select multiple columns return a pandas **DataFrame**

# In[47]:


school_df[["NAME", "ENROLLMENT"]] # multiple columns supplied as a list


# Select row using the `.loc[]` function (**label/index-based**)

# In[48]:


school_df.loc[2] # note that .loc followed by square brackets not parentheses


# Select row using the `.iloc[]` function (**position/order-based**)

# In[49]:


school_df.iloc[2]


# Use `set_index()` to choose a column as index.
# 
# - `inplace=True`
# - reassign the result of `set_index()`

# In[50]:


school_df.set_index('NAME').head()


# In[51]:


school_df.head()


# In[52]:


school_df.set_index('NAME', inplace=True) # or
# school_df = school_df.set_index('NAME')


# In[37]:


school_df.head()


# In[53]:


school_df.loc['FOREST GROVE CHRISTIAN ACADEMY']


# In[54]:


school_df.loc[:, 'ENROLLMENT']


# In[55]:


school_df.iloc[10:20, 1:4]


# In[56]:


school_df.loc['THE ROCK SCHOOL', 'ENROLLMENT']


# ## 4. Selection query on pandas DataFrame
# 
# A single condition returns a Series of booleans again with the same index

# In[57]:


school_df["ENROLLMENT"] > 0


# In[58]:


school_df.ENROLLMENT.head()


# In[59]:


school_df.ENROLLMENT.index.name == school_df.index.name


# In[60]:


school_df.index.values


# In[61]:


school_df.loc[school_df["ENROLLMENT"] > 0] # with loc (recommeneded)


# In[62]:


school_df[school_df["ENROLLMENT"] > 0] # without loc


# For multiple conditions, use **parentheses** to enclose each criterion
# 
# - **AND** operation: `&`
# - **OR** operation: `|`

# In[63]:


school_df[(school_df["ENROLLMENT"] > 0) & (school_df["TEACHERS"] > 0)] # positive enrollment and positive # teachers


# In[64]:


school_df[(school_df["ENROLLMENT"] > 0) | (school_df["TEACHERS"] > 0)]


# ## 5. `groupby()` function
# 
# [groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) is a powerful function to aggregate data.
# 
# A groupby operation involves some combination of splitting the object, **applying a function**, and combining the results.
# 
# This can be used to group large amounts of data and **compute operations on these groups** to understand the subgroups in the data.

# In[75]:


school_df = school_df.loc[(school_df["ENROLLMENT"] > 0) & (school_df["TEACHERS"])]


# In[76]:


school_df.groupby("TYPE")


# In[77]:


by_type = school_df.groupby("TYPE")
by_type.sum()


# <br>

# In[78]:


by_type.max()


# <br>

# In[79]:


school_df.groupby("TYPE").mean()


# <br>

# In[70]:


by_type.agg({'ENROLLMENT': np.sum, 'TEACHERS': np.mean, 'OP_CLASS': 'count'})

