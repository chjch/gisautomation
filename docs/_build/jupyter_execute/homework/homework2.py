#!/usr/bin/env python
# coding: utf-8

# ## Homework 2
# ### Assignment Instruction
# - Work on the following 6 questions.
# - Type your codes only in the cell created for you below the question.
# - Run your codes and see if the output meet the expected result of each question.
# - Your homework will be evaluated by whether I can successfully run your codes and the correctness of the output.
# - Rename this Jupyter Notebook (the .ipynb file) as ```HW2_[LASTNAME].ipynb```, e.g., ```HW2_CHEN.ipynb```.
# - Submit this Jupyter Notebook no later than the deadline posted in the course schedule on Canvas.

# ### 1. Create a list of cities 
# - create a variable, ```city_list```, whose data type is of a Python **list**.
# - the list contains the **names** of the world top 20 populated cities in the table below, retrieved from [Wikipedia](https://en.wikipedia.org/wiki/List_of_largest_cities).
#     
# **<center>[Top 20](https://en.wikipedia.org/wiki/List_of_largest_cities) largest city in the world]</center>**
# 
# | ID | Name           | Country        | Continent     | UN Estimation (2018) | Urban Area |
# |----|----------------|----------------|---------------|----------------------|------------|
# | 1  | Tokyo          |  Japan         | Asia          | 37,400,068           | 4,751      |
# | 2  | Delhi          |  India         | Asia          | 28,514,000           | 14,272     |
# | 3  | Shanghai       |  China         | Asia          | 25,582,000           | 5,436      |
# | 4  | Sao Paulo      |  Brazil        | South America | 21,650,000           | 6,949      |
# | 5  | Mexico City    |  Mexico        | South America | 21,581,000           | 9,017      |
# | 6  | Cairo          |  Egypt         | Africa        | 20,076,000           | 9,844      |
# | 7  | Mumbai         |  India         | Asia          | 19,980,000           | 22,010     |
# | 8  | Beijing        |  China         | Asia          | 19,618,000           | 4,659      |
# | 9  | Dhaka          |  Bangladesh    | Asia          | 19,578,000           | 36,928     |
# | 10 | Osaka          |  Japan         | Asia          | 19,281,000           | 5,129      |
# | 11 | New York       |  United States | North America | 18,819,000           | 684        |
# | 12 | Karachi        |  Pakistan      | Asia          | 15,400,000           | 14,648     |
# | 13 | Buenos Aires   |  Argentina     | South America | 14,967,000           | 5,033      |
# | 14 | Chongqing      |  China         | Asia          | 14,838,000           | 5,378      |
# | 15 | Istanbul       |  Turkey        | Europe        | 14,751,000           | 11,135     |
# | 16 | Kolkata        |  India         | Asia          | 14,681,000           | 13,830     |
# | 17 | Manila         |  Philippines   | Asia          | 13,482,000           | 12,798     |
# | 18 | Lagos          |  Nigeria       | Africa        | 13,463,000           | 7,877      |
# | 19 | Rio de Janeiro |  Brazil        | South America | 13,293,000           | 6,181      |
# | 20 | Tianjin        |  China         | Asia          | 13,215,000           | 3,886      |

# In[1]:


city_list = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mexico City',
             'Cairo', 'Mumbai', 'Beijing', 'Dhaka', 'Osaka', 'New York',
             'Karachi', 'Buenos Aires', 'Chongqing', 'Istanbul', 'Kolkata',
             'Manila', 'Lagos', 'Rio de Janeiro', 'Tianjin']


# ### 2. Calculate the ratio of Asian cities in the list
# - create a new list called ```asian_cities```.
# - create two integer variables that retrieve the length of the two lists respectively. 
# - print the integer variables out. 

# In[ ]:





# - Define a new variable called ```ratio```
# - calculate the ratio by using the two lengths.
# - Your result should be the same as the output of the following cell.

# In[2]:





# ### 3. Indexing and Selecting for list and string
# - Select the 16th item in the ```city_list``` and assign the value to a new variable ```city```.
# - create a new variable, you define its name, that calculates the number of characters in ```city```. 
# - print both variables.

# In[ ]:





# - Convert the ```city``` variable to upper case and lower case and assign the results to ```city_upper``` and ```city_lower``` respectively.
# - print the two new variables

# In[ ]:





# - retrieve the second last item of ```city_list```, note that you cannot use index 19 (use the other way you learned from the lecture).
# - assign the value you retrieved to a new variable ```city2```.
# - concatenate ```city``` and ```city2``` and print the result.

# In[ ]:





# - Select and print out the middle part of the variable ```city```, i.e., characters between the two spaces.
# - To do this, you must use proper start and end indices. 
# - Your output should be the same as the following cell.

# In[3]:





# - reverse the order of the ```city_list``` and assign the value to a new variable ```re_city_list```.
# - print out the value of ```re_city_list```.

# In[ ]:





# ### 4. Iteration using For loop
# - Do a For loop with the ```city_list```.
#     + You can choose either to use a ```range``` object or looping through the list directly.
#     + Print out the city's name if it contains a space in the name. 
#     + Within the for loop, count the number of cities that contains a space in its name.
# - Print the count when the loop is finished.
# - Your result should be the same as the following cell's output.

# In[2]:


for city in city


# In[4]:





# ### 5. Iteration using While loop
# - Do a while loop with the city_list
#     + consider use the length of the city_list
#     + i.e., `while i < len(city_list):`
# - Print out the city's name if it is **not a city in Asia**. Tips are following:
#     + recall the list created in Question 2 `asian_cities`.
#     + within the while loop, you want to check ```if city_list[i] not in asian_cities:```. 
#     + if true, then ```print(city_list[i])```.
# - Your result should be the same as the following cell's output.

# In[5]:





# ### 6. Get user input
# - Ask user to type in a city name
# - based on the user's input, print whether the input is within the ```city_list``` or not.

# In[ ]:




