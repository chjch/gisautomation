#!/usr/bin/env python
# coding: utf-8

# # 3-3: Create Python Functions
# 
# ## 1. What is a function in Python
# 
# - a block of code which only runs when it is called
# - use the `def` keyword
# - pass data, known as arguments, into a function
# - return a result after a series of operations
# 
# ### 1.1 Define a function

# In[1]:


def my_func():
    pass


# In[2]:


my_func


# In[3]:


def hello_world():
    print('hello_world')


# ### 1.2 Run (call) a function

# In[4]:


hello_world


# In[5]:


hello_world()


# ### 1.3 Function with arguments

# In[6]:


def my_func2(pet_name):
    print("I like " + pet_name + ".")


# In[7]:


my_func2("dog")


# ### 1.4 Function returns an  output

# In[8]:


def multiply(a, b):
    return a * b


# In[9]:


multiply(3, 4)


# In[10]:


# assign the output of a function to a variable
result = multiply(3, 4)
print(result)


# ## 2. An Example of a more Pratical Function
# 
# ### 2.1 Convert lat/lon from Degrees Minutes Seconds(DMS) to Decimal Degrees(DD)
# 
# - University of Florida
#     - latitude = 29°38'34.98" N
#     - longitude = 82°21'16.47" W

# In[11]:


def dms_dd(degree, minute, second):
    dd = degree + minute/60 + second/3600
    return dd


# In[12]:


dms_dd(29, 38, 34.98)


# In[13]:


print("latitude is {}, and latitude is {}".format(dms_dd(29, 38, 34.98), -dms_dd(82, 21, 16.74)))


# ### 2.2 How to go from DD to DMS
# 
# Three things to learn:
# 
# 1. Be aware of the precision issue when dealing with floating points
#     + how does ```int()``` function work (truncating)
#     + use the ```round()``` function to round decimals.
# 2. Be comfortable with using `.format()` string.
# 3. The **escape character** in strings `\`.
#     + `\'` --> '
#     + `\"` --> "
#     + `\\` --> \
# 
# 
# Tip:
# - Hold down ```Alt``` key and type 248 on the numeric keyboard.

# In[14]:


print(round(0.7))
print(round(0.5))


# In[15]:


round(3.1415926, 2)


# In[16]:


int(0.7)


# In[17]:


def dd_dms(dd):
    degree = int(dd)
    minute = int((dd - degree) * 60)
    second = round((dd - degree - minute/60) * 3600, 2)
    return "{}°{}'{}\"".format(degree, minute, second)


# In[18]:


print("latitude: {} N.".format(dd_dms(29.64305)))
print("longitude: {} W.".format(dd_dms(82.354575)))


# ## 3. Import a function from another module
# 
# - module: any python code saved in a file (.py)
# - we can store our own Python function in a .py file
# - the function can then be imported as a regular Python module we imported (e.g., random)

# 1. Create a new `.ipynb` file
# 2. Save the `.ipynb` file to a `.py` file
# 3. Import the function from the module

# In[19]:


del dd_dms


# In[20]:


from test_code import dd_dms

