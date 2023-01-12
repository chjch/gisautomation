#!/usr/bin/env python
# coding: utf-8

# # 2-3: Data Types

# ## 1. Numeric (int and float)

# The most straightfoward data type in Python, "what you see is what you get"

# In[1]:


9


# In[2]:


x = 6


# In[3]:


y = 1.5


# In[4]:


z = x + y
z


# In[5]:


z = x/y
z


# ## 2. String

# In Python, string is defined by enclosing quotes (single/double) around texts.

# In[6]:


"Welcome to ArcGIS Pro customization"


# In[7]:


'Welcome to ArcGIS Pro customization'


# - ```""``` is an empty string; 
# - ```" "``` is a space which is also a string.
# - A double quoted string can contain single quotes and vice versa.

# In[8]:


print("I'm starting to learn Python.") 


# In[9]:


print('Albert Einstein said: "You never fail until you stop trying."')


# ## 3. String Operations

# ### 3.1 Concatenating

# In[10]:


# concatnating
s1 = "Welcome to"
s2 = "ArcGIS Pro customization"
s1 + s2


# ### 3.2 Indexing and Slicing

# In[11]:


# indexing
s3 = s1 + s2
print(s3)


# In[12]:


# slicing
print(s3[10:16]) # start and end indexes to retrieve the word "ArcGIS"


# ```{admonition} Note 
# - In Python, and most of other programming languages, index starts from 0.
# - String **_slicing_**: start (from) index is **included**, and end (to) index **not included**.
# ```

# In[13]:


print(s3[:7]) # skip the start index
print(s3[21:]) # skip the end index


# In[14]:


s3[:10] + " " + s3[10:] # fixing the space in last string


# 

# In[15]:


# slicing with steps
s4 = "0123456789"
print(s4[1::2])


# ### 3.3 Basic String Functions: upper, lower, str

# In[16]:


s5 = 'abcdefghijklmnopqrstuvwxyz'
s5.upper() # change to upper case


# In[17]:


s5


# In[18]:


s5 = s5.upper()


# In[19]:


s5


# In[20]:


s5.lower()


# In[21]:


hw_name = "Changjie's Homework"
num = 1
hw_name + num


# In[22]:


hw_name + str(num) # convert an object from other types of data to string


# ## 4. Making Sense of Python Variables

# - Variable is a container of data. 
# - Unlike other programming languages, **Python has no explicit command** for declaring a variable.
# - A variable is created the moment you first assign a value to it.
#     + no need to specify its type. Python will figure it out automatically.
# - After the creation of a variable, it can be _referenced_, _modified_ and _deleted_. 

# ```{admonition} Note
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# ```

# - Naming Rules:
#     + A variable name must start with a letter or the underscore character;
#     + A variable name **cannot start with a number**; 
#     + A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ );
#     + Variable names are case-sensitive (**_age_**, **_Age_** and **_AGE_** are **<u>3 different variables</u>**).
#     + There are some reserved words which you should not use as a variable.

# ### 4.1 Declare a variable

# In[22]:


my_name = "Michael"
_my_name = "Michael"
__my__name = "Michael"
myName = "Michael"
MyName = "Michael"


# In[ ]:


# illegal names
my name = "Michael" # space is invalid
my-name = "Michael" # dash is invalid (all special characters)
1st_name = "Michael" # starting with a number is invalid


# - Good naming strategy:
#     + Choose meaningful name instead of short name. ```num_course``` is better than ```nc```.
#     + Maintain the length of a variable name. ```number_of_courses_in_spring2020``` is too long.
#     + Be consistent; ```num_course``` or ```numCourse``` or ```NumCourse```.
# - [PEP 8 -- style guide for Python code](https://www.python.org/dev/peps/pep-0008/)

# ### 4.2 Declare Multiple Variables Simultaneously

# In[1]:


a, b, c = "Orlando", 2, "Gainesville"
print(a)
print(b)
print(c)


# In[2]:


x = y = z = 100
print(x)
print(y); print(z)


# ## 5. Boolean

# In[ ]:


True


# In[ ]:


False


# ### 5.1 Logical Operator

# In[ ]:


True or False # Returns True if one of the statements is true


# In[ ]:


True and False # Returns True if both statements are true


# In[ ]:


not True # Reverse the result


# ### 5.2 Comparison Operator

# In[27]:


1 == True


# In[26]:


0 == False


# [Python Operators](https://www.w3schools.com/python/python_operators.asp)

# In[3]:


b > 3


# ## 6. List

# In[95]:


city_list = ['Gainesville', 'Orlando', 'Miami', 'Tampa']
city_list


# In[ ]:


city_list = ['Gaiensville', 'Orlando', 'Miami', 4, True] # a list can contains more than one data types of Python data
city_list


# In[32]:


len(cities) # return the number of elements in the list


# ### 6.1 Indexing and Slicing

# In[ ]:


two_cities = cities[0:2]
print(two_cities)
two_cities = cities[:2]
print(two_cities)


# In[ ]:


city_list[:4]
city_list[-1]
city_list[::2]

