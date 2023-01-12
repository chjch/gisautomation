#!/usr/bin/env python
# coding: utf-8

# # Homework 5
# 
# ## Assignment
# 
# ## 1. NumPy

# ### <span>**<font color='royalblue'>Question 1.1</font>**</span>
# 
# Describe your answer to the question: "what is NumPy?" in a short paragraph (2-4 sentences).

# `# write markdown below (and then render it Ctrl + Enter)`
# 
# NumPy is a Python package for data analysis. 

# ### <span>**<font color='royalblue'>Question 1.2</font>**</span>
# 
# Import numpy (recall the convention)

# In[1]:


# Write your codes below
import numpy as np


# ### <span>**<font color='royalblue'>Question 1.3</font>**</span>
# 
# Create a numpy ndarray that contains even numbers between 0 and 9. (using only numpy function)

# In[2]:


# Write your codes below
np.arange(0, 10, 2)


# ### <span>**<font color='royalblue'>Question 1.4</font>**</span>
# 
# Create a sequence of numbers with **0.5** constant increment between 0 and 50 (i.e., 0, 0.5, 1, 1.5, ..., 49.5, 50). (using only numpy function)

# In[3]:


np.linspace(0, 50, 101)


# In[4]:


# Write your codes below


# ### <span>**<font color='royalblue'>Question 1.5</font>**</span>
# 
# Create a **4x4** 2-d array with **random numbers** in a _uniform distribution_ in the range \[0, 1).

# In[5]:


np.random.rand(4,4)


# In[6]:


np.random.rand(4,4,2)


# In[7]:


# Write your codes below

(np.random.rand(4,4) * 10).astype(int)


# ### <span>**<font color='royalblue'>Question 1.6</font>**</span>
# 
# 1. Import **arcpy** and set up the **workspace** to  your local _class geodatabase_, i.e., `class_data.gdb`.
# 2. Create a variable that references the `crash` feature class in the geodatabase. 

# In[8]:


# Write your codes below

import arcpy

gdb_worksp = r"D:\Dropbox (UFL)\URP6271\urp6271_spring2022\class_data.gdb"
arcpy.env.workspace = gdb_worksp
crash_fc = 'crash'


# ### <span>**<font color='royalblue'>Question 1.7</font>**</span>
# 
# 1. Retrive and print out all the field names (as a Python List) in the `crash` feature class.
# 2. Convert the `crash` feature class to a (_Structured_) NumPy array with the following fields.
# 
# ```python
# crash_fields = ['City', 'Crash_Type', 'Vehicles', 'Non_Motorists', 'Fatalities', 'Injuries',
#                 'Alcohol_Related', 'Distraction_Related', 'Drug_Related', 'Estimated_Damages',
#                 'Weather_Condition', 'Light_Condition', 'Crash_Severity', 'Manner_of_Collision',
#                 'Type_of_Intersection', 'Passengers', 'Bicyclists', 'Pedestrians', 'Citations',
#                 'Property_Dmg_Amt','Vehicle_Dmg_Amt']
# ```
# 3. Store the structured array with a variable named: `crash_arr`. 
# 4. Find out and **print** how many records (rows) in the `crash_arr`.

# In[9]:


crash_fields = []
for field in arcpy.ListFields(crash_fc):
    crash_fields.append(field.name)
print(crash_fields)


# In[10]:


# Write your codes below
crash_fields = [field.name for field in arcpy.ListFields(crash_fc)] # list comprehension
print(crash_fields)


# In[11]:


# Write your codes below (feel free to add/delete cells if necessary)
crash_fields = ['City', 'Crash_Type', 'Vehicles', 'Non_Motorists', 'Fatalities', 'Injuries',
                'Alcohol_Related', 'Distraction_Related', 'Drug_Related', 'Estimated_Damages',
                'Weather_Condition', 'Light_Condition', 'Crash_Severity', 'Manner_of_Collision',
                'Type_of_Intersection', 'Passengers', 'Bicyclists', 'Pedestrians', 'Citations',
                'Property_Dmg_Amt','Vehicle_Dmg_Amt']
crash_arr = arcpy.da.FeatureClassToNumPyArray(crash_fc, crash_fields)


# In[12]:


crash_arr.shape


# ### <span>**<font color='royalblue'>Question 1.8</font>**</span>
# 
# 1. Retrieve the first 7 elements of `crash_arr`.
# 2. Grab (retrieve and store as a variable) the first, fourth, eighth, 12th, 50th, 100th row of the array.
# 3. Grab the column `Fatalities` from the array.

# In[13]:


# Write your codes below
crash_arr[:7]


# In[14]:


np.array((0,3,7,11))


# In[15]:


crash_arr[np.array((0,3,7,11))]


# In[16]:


crash_arr['Crash_Type']


# ### <span>**<font color='royalblue'>Question 1.9</font>**</span>
# 
# 1. How many crashes have positive fatalities in this dataset?
# 2. What is the maximum value of fatatlities in the data?
# 3. How many total fatalities in the dataset?

# In[17]:


# Write your codes below
crash_arr[crash_arr['Fatalities'] > 0].shape


# In[18]:


# Write your codes below
np.max(crash_arr['Fatalities'])


# In[19]:


crash_arr['Fatalities'].max()


# In[20]:


crash_arr['Fatalities'].sum()


# ### <span>**<font color='royalblue'>Question 1.10</font>**</span>
# 
# 1. The **total Damage** of an accident is considered property damage plus vehicle damage. Create a new array that adds the two fields together.
# 2. What is the average value (mean) of total damage per crash? What about the standard deviation? 
# 3. Find out the maximum **total damage** in this dataset; what was the **_weather condition_** and which **_city_** did it occur?

# In[21]:


# Write your codes below
total_damage = crash_arr['Property_Dmg_Amt'] + crash_arr['Vehicle_Dmg_Amt']


# In[22]:


print(total_damage)


# In[23]:


np.mean(total_damage)


# In[24]:


np.std(total_damage)


# In[25]:


import matplotlib.pyplot as plt


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


fig, ax = plt.subplots()

ax.hist(total_damage)


# In[28]:


# Write your codes below
crash_arr[total_damage.argmax()]['Weather_Condition']


# In[29]:


crash_arr[total_damage.argmax()]['City']


# ## 1. Pandas

# ### <span>**<font color='royalblue'>Question 2.1</font>**</span>
# 
# Describe your answer to the question: "what is Pandas?" in a short paragraph (2-4 sentences).

# `# write markdown below (and then render it Ctrl + Enter)`
# 
# Pandas is a Python package for data analysis. Offers a flexible data struture, such as DataFrame, Series to do panel data. It's the "excel sheet" for Python.

# ### <span>**<font color='royalblue'>Question 2.2</font>**</span>
# 
# import pandas (recall the convention and import numpy first)

# In[30]:


# Write your codes below

import numpy as np
import pandas as pd


# ### <span>**<font color='royalblue'>Question 2.3</font>**</span>
# 
# Convert the **total damage** array to a pandas `Series`

# In[31]:


# Write your codes below
pd.Series(total_damage)


# ### <span>**<font color='royalblue'>Question 2.4</font>**</span>
# 
# 1. Convert the `crash_arr` array to a pandas `DataFrame` with the name `crash_df`.
# 2. Preview the first 5 elements.
# 3. Preview the last 8 elements.

# In[32]:


# Write your codes below
crash_df = pd.DataFrame(crash_arr)


# In[33]:


# Write your codes below
crash_df.head()


# In[34]:


# Write your codes below
crash_df.tail(8)


# ### <span>**<font color='royalblue'>Question 2.5</font>**</span>
# 
# 1. Retrive columns \['Alcohol_Related', 'Drug_Related', 'Injuries'\] from `crash_df`.
#     1. Using label indexing.
#     2. Using location/position based indexing.
# 2. Assign these columns to a new dataframe variable (call the variable with a name you preferred).
# 3. How many crashes are **alcohol related**? How about **drug related**?
# 4. Driving Under Impact (DUI) is a criminal (not civil) charge (up to 6 months in jail first caught). Both drug or alcohol exceeding certain limit are considered DUI. In this dataset, what is the percentage of DUI-related crashes?

# In[35]:


# Write your codes below
crash_df[['Alcohol_Related', 'Drug_Related', 'Injuries']]


# In[36]:


crash_df.iloc[9:19, [5, 6, 8]]


# In[37]:


crash_subdf = crash_df.loc[:, ['Alcohol_Related', 'Drug_Related', 'Injuries']]


# In[38]:


# Write your codes below
crash_subdf.loc[crash_subdf['Alcohol_Related'] == 'Y']


# In[39]:


(crash_subdf['Alcohol_Related'] == 'Y').value_counts()


# In[40]:


np.sum(crash_subdf['Alcohol_Related'] == 'Y')


# In[41]:


crash_subdf


# In[42]:


# Write your codes below
(crash_subdf['Drug_Related'] == 'Y').value_counts()


# In[43]:


371 + 108 - 59


# In[44]:


# Write your codes below (again feel free to add/delete cells)
crash_df.loc[(crash_subdf['Drug_Related'] == 'Y') | 
             (crash_subdf['Alcohol_Related'] == 'Y')]


# In[45]:


len(crash_df.loc[(crash_subdf['Drug_Related'] == 'Y') | 
             (crash_subdf['Alcohol_Related'] == 'Y')]) / len(crash_subdf)


# ### <span>**<font color='royalblue'>Question 2.6</font>**</span>
# 
# 1. Aggregate `crash_df` by "City" and then calculated the **sum**?
# 2. Which **city** has the most number of citations?

# In[46]:


# Write your codes below
by_city_crash = crash_df.groupby('City')


# In[47]:


by_city_crash.sum()


# In[48]:


by_city_crash.sum()['Citations'].idxmax()


# ### <span>**<font color='royalblue'>Question 2.7</font>**</span>
# 
# 1. Aggregate `crash_df` by "Alcohol_Related" and then calculated the **mean** for "Estimated_Damages"?
# 2. What do you find out?
# 3. Aggregate `crash_df` by "Drug_Related" and then calculated the **mean** for "Estimated_Damages"?
# 4. What do you find out?
# 5. Was Drug-related or Alcohol-related crashes cost more damage?
# 6. Was alcohol-related crash or drug-related crash more fatal? How many people were dead (per 100 crashes) for each category? (Show the codes you used to find out the answer)

# In[49]:


# Write your codes below
crash_df.groupby('Alcohol_Related').mean()['Estimated_Damages']


# In[50]:


crash_df.groupby('Alcohol_Related').mean()['Estimated_Damages']


# In[51]:


# Write your codes below
crash_df.groupby('Drug_Related').mean()['Estimated_Damages']


# In[52]:


# Write your codes below
crash_df.groupby('Drug_Related').mean()['Fatalities']


# In[53]:


crash_df.groupby('Drug_Related').mean()['Fatalities'] * 100


# In[54]:


# Write your codes below (again feel free to add/delete cells)
crash_df.groupby('Alcohol_Related').mean()['Fatalities']


# In[55]:


# Write your codes below (again feel free to add/delete cells)
crash_df.groupby('Alcohol_Related').sum()['Fatalities']


# In[56]:


crash_df.groupby('Drug_Related').sum()['Fatalities']


# In[57]:


# Write your codes below (again feel free to add/delete cells)
crash_df.groupby('Alcohol_Related').mean()['Fatalities'] * 100

