#!/usr/bin/env python
# coding: utf-8

# # 5-1: Using NumPy for ArcGIS
# 
# - NumPy: a numeric computing libary: multidimensional array, linear algebra, mathematical operation
# - Offer fast operation of n-dimensional array
# - The foundation of the Scientific Python Ecosystem
#     - pandas
#     - SciPy
#     - matplotlib
#     - Seaborn
#     - scikit-learn
#     - IPython
#     - NetworkX
#     - Statsmodel
#     
# Helpful resource on NumPy:
# - [NumPy official site](https://numpy.org/)
# - [Tutorials on the scientific Python ecosystem](http://scipy-lectures.org/intro/numpy/index.html)

# ## 1. import the NumPy package

# In[1]:


import numpy as np # this is a convention


# ## 2. Get started with the basics
# 
# ### 2.1 Recall a Python list
# 
# - Converting list to numpy ndarray using `np.array()`

# In[2]:


my_list = [1, 2, 3, 4]
my_list


# In[3]:


my_list = list(range(1, 5))
my_list


# In[4]:


np.array(my_list) 


# In[5]:


type(np.array(my_list))


# - Create ndarray with `np.arange()`: control interval width

# In[6]:


np.arange(1, 5)


# In[7]:


np.arange(10)   # default is start from 0


# In[8]:


np.arange(0, 10)


# In[9]:


np.arange(0, 10, 2)


# - Create ndarray the `np.linspace()`: controlling number of elements

# In[10]:


np.linspace(1, 5, 5) # start, stop, num


# In[11]:


np.linspace(0, 5, 11)   # (5-0)/(11-1)


# In[12]:


np.linspace(0, 5, 21)


# In[13]:


np.linspace(0, 5, 26)   # it requires a lot more codes without numpy i.e., using loop


# ### 2.2 Indexing and slicing on NumPy array
# 
# - index starts with "**0**" as usual
# - a negative index start count from the end of the array
# - use the colon to get multiple elements and return as an array
# - we can also slice NumPy array with step

# In[14]:


my_arr = np.arange(10)
my_arr


# In[15]:


my_arr[4]


# In[16]:


my_arr[-2]


# In[17]:


my_arr[1:6]


# In[18]:


my_arr[1:6:2]


# In[19]:


my_arr[:]


# In[20]:


my_arr[::-1]


# ## 3. Generate random numbers with NumPy

# In[21]:


np.random.randint(2, 10)


# In[22]:


np.random.randint(10)


# In[23]:


np.random.randint(0, 10, 20)


# In[24]:


np.random.rand(3,2) # from a uniform distribution over `[0, 1)`


# ## 4. Work with NumPy in ArcGIS

# In[25]:


import arcpy


# In[26]:


gdb_worksp = r"D:\Dropbox (UFL)\URP6271\urp6271_spring2022\class_data.gdb"
arcpy.env.workspace = gdb_worksp


# In[27]:


arcpy.ListFeatureClasses()


# In[28]:


school_fc = "schools"


# ### 4.1 Retrieve field names of a feature class `arcpy.ListFields()`
# 
# - a [field object](https://pro.arcgis.com/en/pro-app/2.7/arcpy/classes/field.htm)
# - Code example:
# 
# ```python
# import arcpy
# 
# feature_class = "c:/data/counties.shp"
# 
# # Create a list of fields using the ListFields function
# fields = arcpy.ListFields(feature_class)
# 
# # Iterate through the list of fields
# for field in fields:
#     # Print field properties
#     print("Field:       {0}".format(field.name))
#     print("Alias:       {0}".format(field.aliasName))
#     print("Type:        {0}".format(field.type))
#     print("Is Editable: {0}".format(field.editable))
#     print("Required:    {0}".format(field.required))
#     print("Scale:       {0}".format(field.scale))
#     print("Precision:   {0}".format(field.precision))
# ```

# In[29]:


school_fields = []
for field in arcpy.ListFields(school_fc):
    school_fields.append(field.name)
print(school_fields)


# ### 4.2 Convert a feature class to NumPy array
# 
# - `arcpy.da`: the **_[Data Access](https://pro.arcgis.com/en/pro-app/2.8/arcpy/data-access/what-is-the-data-access-module-.htm)_** module
# - `arcpy.da.FeatureClassToNumPyArray` converts a feature class to a **_Structured Array_**
# - learn more about [structured arrays](https://docs.scipy.org/doc/numpy/user/basics.rec.html) 

# In[30]:


school_arr = arcpy.da.FeatureClassToNumPyArray(
    school_fc, ["NAME", 'OP_CLASS', 'ENROLLMENT', 'TYPE', 'TEACHERS']
)


# In[31]:


school_arr


# Retrieve the **shape** (or length) of an array

# In[32]:


len(school_arr)


# In[33]:


school_arr.shape


# View the first five elements of a structured array

# In[34]:


school_arr[:5]


# In[35]:


school_arr[0:5]


# View the 1st, 5th, 10th, 100th element of the array
# 
# - supply the indicies as a Python list

# In[36]:


school_arr[[0, 4, 9, 99]]


# Retrieve a **field** (column) from a structured array: using the field name

# In[37]:


school_arr['ENROLLMENT']


# ### 4.3 Compute statistics of an ndarray
# 
# - maximum: ```np.max()```
# - minimum: ```np.min()```
# - mean: ```np.mean()```
# - standard deviation: ```np.std()```

# In[38]:


enroll_arr = school_arr['ENROLLMENT']


# In[39]:


np.max(enroll_arr)


# In[40]:


np.min(enroll_arr)


# In[41]:


np.mean(enroll_arr)


# In[42]:


np.std(enroll_arr)


# ### 4.4 Simple Query against NumPy array
# 
# - which school has the largest enrollment: `argmax`
# - which school has the smallest enrollment: `argmin`

# In[43]:


enroll_arr.argmax() # returns the index of the largest value


# In[44]:


school_arr['NAME'][enroll_arr.argmax()]


# In[45]:


school_arr['NAME'][enroll_arr.argmin()]


# ### 4.5 Generate new arrays based on a conditional statement
# 
# - schools enrollment is positive
# - schools that are public

# In[46]:


enroll_arr > 0 # returns as an ndarray of booleans


# In[47]:


school_type_arr = school_arr['OP_CLASS']
school_type_arr == 'PUBLIC'


# Use array of booleans to select from an ndarray
# 
# - the array of booleans must be in the same shape as the original array

# In[48]:


num_arr = np.array([1, 2, 3, 4])
num_arr


# In[49]:


bool_arr = np.array([True, False, True, True])


# In[50]:


num_arr[bool_arr]


# In[51]:


# How to find out which school doesn't have positive enrollment
# np.invert() negates the judgement
school_arr[np.invert(enroll_arr > 0)]['NAME']


# ### 4.6 Simple numeric operation 
# 
# - operation on its own
# - operation including two arrays (must be of the same shape)

# In[52]:


enroll_arr


# In[53]:


enroll_arr * 2


# In[54]:


enroll_arr + 100


# In[55]:


pos_school_arr = school_arr[school_arr['ENROLLMENT'] > 0]


# In[56]:


# ratio of number of teachers and students
pos_school_arr["TEACHERS"] / pos_school_arr["ENROLLMENT"]


# In[57]:


(pos_school_arr["TEACHERS"] / pos_school_arr["ENROLLMENT"]).argmax()


# In[58]:


pos_school_arr['NAME'][(pos_school_arr["TEACHERS"] / pos_school_arr["ENROLLMENT"]).argmax()]

