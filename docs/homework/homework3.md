# Homework 3

## Assignment Instruction

- Create a new Jupyter Notebook file to work on the following questions.
- Run your codes to ensure the output is the same as the expected result of each question.
- Rename your Jupyter Notebook (the `.ipynb` file) as `HW3_<LASTNAME>.ipynb`, e.g., `HW3_CHEN.ipynb`.
- Submit this Jupyter Notebook no later than the deadline posted in the course schedule on Canvas.

## Question 1:

Write a Python program that checks the value of a variable temperature. If the temperature is greater than or equal to 100, the program should print "Boiling Point". If the temperature is less than 100 but greater than or equal to 0, it should print "Liquid". If the temperature is below 0, it should print "Freezing".

**Sample Output**:

```python
temperature = 50  # You can change this number to test with other values
# should print "Liquid"
```

**Expected Concepts to be Used**:

- Variables
- If-Else statement
- Comparison operators

# Question 2:

Define a Python **_function_** named `calculate_area` that takes the
$base$ and $height$ of a triangle as arguments and **returns** the _area of the triangle_.
Remember, the formula for the area of a triangle is: $\frac{1}{2} \times base \times height$.
Then, write a `print` statement with either `.format` or "f-string" to print out the
message

**Sample Output**:

```python
calculate_area(10, 5)
# should print "Area of the triangle with base 10 and height 5 is 25.0."
```

**Expected Concepts to be Used**:

- Function definition
- Parameters and arguments
- Return statement
- Arithmetic operations

## Question 3:

Write a Python **function** named `evaluate_zone` that takes two arguments:
`zone_type` (a string) and `population_density` (a number).
The function should return recommendations for urban planning based on the following conditions:

- If `zone_type` is "Residential" and `population_density` is greater than **1000**, 
  return "High-density residential area. Consider infrastructure for high population."
- If `zone_type` is "Residential" and `population_density` is **1000** or less, 
  return "Low-density residential area. Focus on community services."
- If `zone_type` is "Commercial" and `population_density` is greater than **500**,
  return "High-density commercial area. Prioritize business development and public transportation."
- If `zone_type` is "Commercial" and `population_density` is **500** or less,
  return "Low-density commercial area. Encourage local businesses and pedestrian-friendly spaces."
- In all other cases, return "Zone type not recognized."

**Sample Output**:

```python
print(evaluate_zone("Residential", 1500))
# Should print "High-density residential area. Consider infrastructure for high population."

print(evaluate_zone("Commercial", 300))
# Should print "Low-density commercial area. Encourage local businesses and pedestrian-friendly spaces."

print(evaluate_zone("Industrial", 800))
# Should print "Zone type not recognized."
```

**Expected Concepts to be Used**:

- Function definition
- If-Else statement with compound conditions
- Parameters and arguments
- String operations
- Return statement