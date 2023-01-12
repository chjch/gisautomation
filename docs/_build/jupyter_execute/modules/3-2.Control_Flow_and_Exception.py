#!/usr/bin/env python
# coding: utf-8

# # 3-2: More Control Flow and Python Exceptions
# 
# ## 1. Control Flow Statements

# In[1]:


import random
x = random.randint(1, 6)


# ### 1.1 `break` statement terminate the loop

# In[2]:


# example of break statement (same script from last module)
num_guess = 3

while num_guess > 0:
    guess = int(input("Enter a number between 1 and 6: "))
    num_guess -= 1
    if x > guess:
        print("Try larger.")
    elif x < guess:
        print("Try smaller.")
    else:
        print("Bingo!")
        break  # using break to terminate the loop although num_guess > 0
        
    if num_guess > 0:
        print(str(num_guess) + " more guesses left.")
    else:
        print("Sorry, no more guesses.")


# ### 1.2 `continue` statement move on to the next iteration
# 
# The following example allows us to validate the input before evaluate the value of the input number.

# In[ ]:


num_guess = 3
while num_guess > 0:
    guess = int(input("Enter a number between 1 and 6: "))
    
    if guess > 6 or guess < 1:
        print("Your input is out of range")
        continue
    
    num_guess -= 1
    
    if x > guess:
        hint = "Try larger. "
    elif x < guess:
        hint = "Try smaller. "
    else:
        print("Bingo!")
        break      
        
    if num_guess > 0:
        print(hint + str(num_guess) + " more guesses left.")
    else:
        print("You guessed wrong, no more guesses.")


# ### 1.3 `pass` statement
# 
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. 

# In[ ]:


num_guess = 3
while num_guess > 0:
    guess = int(input("Enter a number between 1 and 6: "))
    num_guess -= 1
    
    if guess > 6 or guess < 1:
        print("Your input is out of range")
        continue
    else:
        if x > guess:
            hint = "Try larger. "
        elif x < guess:
            hint = "Try smaller. "
        else:
            print("Bingo!")
            break      
        
    if num_guess > 0:
        print(hint + str(num_guess) + " more guesses left.")
    else:
        pass
    
else: # else on exhaustion of loop
    print("You guessed wrong, no more guesses.")


# In[ ]:


def my_func():
    pass  # a placeholder## Section 3 - Exceptions in Python
In general, two types of errors we can encounter in Python:
- **syntax error**: also known as _parsing_ error, the _Python interprter_ cannot parse the codes to machine language.
- **exception**: _syntactically correct_, cause an error when an attempt is made to execute the codes.


# ## 2. Exceptions
# In general, two types of errors we can encounter in Python:
# - **syntax error**: also known as _parsing_ error, the _Python interprter_ cannot parse the codes to machine language.
# - **exception**: _syntactically correct_, cause an error when an attempt is made to execute the codes.

# ### 2.1 Syntax Error
# - most common complaint you get while you are still learning Python
# - checked first before all exceptions
# - Examples:
#     + in `if` statement, use assignment operator, `=`, rather than comparison operator `==`.
#     + "if-else" without colon, `:`.
#     + `else` without a `if`
#     + define string with just one quote, or mixed the quotes
#     + mistyped dots e.g., 1.3.2
#     
# **Can you point out the error in the following code**?

# In[ ]:


a = 3.4
if a = 3
    print("a is equal to 3")
elif:
    print("a is not equal to 3')


# ``` {admonition} Note:
# Syntax error were checked first because _Python Interpreter_ first converts Python code to machine code
# ```

# ### 2.2  Exceptions
# 
# **Type Error**
# 
# - pass a list where a number or string is expected
# - more arguments received

# In[ ]:


int(['3.4'])


# **Name Error**
# 
# - A typo in Python keywords
# - A variable is called before it get defined

# **Zero Division Error**

# In[ ]:


print(3 / 0)


# **Attribute Error**
# 
# - An object does not have the attribute called.m

# In[ ]:


"a".upper()


# In[ ]:


["a"].upper()


# **Value Error**
# 
# - Cannot convert something
# - useful when checking whether the input is numeric

# In[ ]:


float("3")


# In[ ]:


float("d")


# In[ ]:


num = input("Please enter a number: ")
print(float(num))


# ## 3. Exception Handling
# 
# Customize the behavior when an exception occured. Using the `try`-`except` statement
# ```
# try:
#     some Python
#     statements
# except:
#     what to do 
#     if exception is raised
# ```

# In[ ]:


try:
    guess = int(input("Enter a number between 1 and 6: "))
except ValueError:
    print("Invalid number")

