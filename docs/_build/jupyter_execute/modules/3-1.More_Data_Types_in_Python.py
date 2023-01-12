#!/usr/bin/env python
# coding: utf-8

# # 3-1: More Data Types
# 
# ## 1. Tuple

# In[1]:


t = (1, 2, 3)


# In[2]:


t[0]


# ### 1.1 Tuple unpacking

# In[3]:


a, b = (1, 2)


# In[4]:


print(a)
print(b)


# ### 1.2 Convert tuple to list

# In[5]:


fl_city_list = ["Gainesville", "Orlando", "Tampa"]
fl_city_list


# In[6]:


fl_city_tuple = tuple(fl_city_list)
fl_city_tuple


# In[7]:


list(fl_city_tuple) # convert back from tuple to list


# ### 1.3 Tuple is immutable
# 
# Unlike list, once a tuple is created it cannot be changed

# In[8]:


t[1] = 5


# In[10]:


fl_city_list.append('Jacksonville')
fl_city_list


# In[11]:


fl_city_tuple.append('Jacksonville')


# ## 2. Set
# 
# Unique collection of elements

# In[12]:


s = {1,2,3}


# In[13]:


s[0]


# In[13]:


for fl_city in ['Miami', 'Orlando', 'Boca Raton', 'Tampa']:
    fl_city_list.append(fl_city)
    print(fl_city_list)


# In[14]:


set(fl_city_list)


# In[15]:


for city in fl_city_list:
    print('I like ' + city)


# In[16]:


for city in set(fl_city_list):
    print('I like ' + city)


# ## 3. Dictionary
# 
# Consists of a collection of `{key: value}` pairs wrapped around by curly brackets.

# In[17]:


my_dict = {'institution': 'University of Florida',
           'college': 'Design, Construction, and Planning',
           'enrollment year': 2022, 
           'graduate': True}
my_dict


# ### 3.1 Indexing and selecting

# In[18]:


my_dict['college']


# ``` {admonition} Note: 
# For dictionaries, you cannot use position for indexing purpose.
# ```

# In[19]:


my_dict[0] 


# ### 3.2 Keys and values

# In[20]:


my_dict.keys()


# In[21]:


my_dict.values()


# In[22]:


for key in my_dict.keys():
    print(my_dict[key])


# In[23]:


for key, value in my_dict.items():
    print('the value of ' + key + 'is ' + value) # what is the problem and how to fix it


# ### 3.3 Dict with a list value

# In[24]:


city_dict = {"FL": ["Gainesville", "Orlando", "Tampa"],
             "CA": ["San Francisco", "Los Angeles"], 
             "TA": ["Houston", "San Antonio"]}


# In[25]:


city_dict['FL'][0]


# ## 4. `format` function

# In[26]:


for key, value in my_dict.items():
    print('the value of {} is {}'.format(key, value)) # what is the problem and how to fix it


# In[27]:


for key, value in my_dict.items():
    print('the value of {} is {}'.format(key.upper(), value)) # what is the problem and how to fix it


# ## 5. List comprehension 
# 
# An elegant way to iterate through a list

# In[28]:


[print(city) for city in fl_city_list]


# In[29]:


x = [1, 2, 3, 4]


# In[30]:


out = []
for item in x:
    out.append(item**2)
print(out)


# In[31]:


[item**2 for item in x]

