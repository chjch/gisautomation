#!/usr/bin/env python
# coding: utf-8

# # 2-4: Control (Flow) Structure

# ## 1. Conditional Statement

# In[1]:


a = '-'
print(a == '+')     # is a equal to plus sign


# ``` {admonition} **Note**: 
# - "=" is an assignment operator.
# - "==" is a comparison operator.
# ```

# ### 1.1 If statement

# In[2]:


if a == '-':
    print('yes')


# ### 1.2 If-else compound statements (block)

# In[3]:


if a == '+':
    print('a is a plus sign')
else:
    print('a is a minus sign')


# ``` {admonition} **Note**:
# In Python, we use **indentation** to define the structure, or the flow, of code execution.<br><br>
# The **colon** after the **if** statement is required. Most code blocks, such as _loop_ and _function_ start by a **colon**.
# ```

# ### 1.3 if-elif-else block

# In[4]:


if a == '+':
    print('a is a plus sign')
elif a == "-":
    print('a is a minus sign')
else:
    print('a is neither a plus nor a minus sign')


# ### 1.4 Comparing Numbers

# In[5]:


first_number = 20
second_number = 20
if first_number > second_number:
    print(str(first_number) + " is greater than " + str(second_number)) 
elif first_number < second_number:
    print(str(first_number) + " is smaller than " + str(second_number))
else:  
    print(str(first_number) + " is equmal to " + str(second_number))


# In[6]:


# dynamic user inputs
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number > second_number:
    print(str(first_number) + " is greater than " + str(second_number))
elif first_number < second_number:
    print(str(first_number) + " is smaller than " + str(second_number))
else:
    print(str(first_number) + " is equal to " + str(second_number))


# In[12]:


# without converting to integers
'45' > '245'


# ### 1.5 Logical Operators in Conditional Statement

# In[13]:


first_number = int(input("Enter first number: "))

if first_number > 10:
    print(str(first_number) + " is greater than 10.")
elif first_number > 5 and first_number <= 10:
    print(str(first_number) + " is smaller or equal to 10 but greater than 5.")
elif first_number > 0 and first_number <= 5:
    print(str(first_number) + " is smaller or equal to 5 but greater than 0.")
else:
    print(str(first_number) + " is negative.")


# ## 2. Loop (Iteration)

# ### 2.1 For Loop
# 
# For loop with a **range** object

# In[ ]:


range(4)


# In[ ]:


range(1, 4)


# In[ ]:


list(range(1, 10, 2))


# In[ ]:


list(range(4, 1, -1))


# In[ ]:


# sum up value from 1 to 4.
total = 0
for i in range(4):
    print("i is " + str(i))
    total = total + i
    print("sum is " + str(total))
print("program done.")


# ``` {admonition} **Note**: 
# "sum" is a reserved word in python. It is a function, so avoid using it for variable names.
# ```

# For loop with a **list** object

# In[15]:


cities = ['Gainesville', 'Miami', 'Orlando', 'Tampa']
for city in cities:  # city is just a pointer it can have any name abiding by the rules
    print("I like " + city)


# ### 2.2 While Loop

# Calculate the **total sum from 1 to 100**.

# In[19]:


i = 1
total = 0
while i <= 100:
    # print("i is " + str(i))
    total = total + i
    i += 1 # same as i = i + 1
print("Final sum is " + str(total))


# ``` {admonition} **Note**
# The difference between for and while loop is whether the number of iteration is known.
# ```

# In[20]:


my_bool = True
while my_bool:
    x = input("Please enter a number: ")
    if x == "3":
        my_bool = False
print("program finished.")


# ## 3. Guess a Randomly Generated Integer

# In[21]:


import random


# In[24]:


# generate a random integer between 1 and 6, i.e., 1, 2, 3, 4, 5, 6

print(x)


# ```{admonition} Tip:
# :class: tip
# - ```tab``` to **auto**complete code
# - ```Shift + tab``` to view the documentation
# ```

# In[1]:


x = random.randint(1, 6)
num_guess = 5

while num_guess > 0:
    guess = int(input("Enter a number between 1 and 6: "))
    num_guess -= 1
    if x > guess:
        print("Try larger.")
    elif x < guess:
        print("Try smaller.")
    else:
        print("Bingo!")
        break    
        
    if num_guess > 0:
        print(str(num_guess) + " more guesses left.")
    else:
        print("Sorry, no more guesses.")


# In[ ]:




