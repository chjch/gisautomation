# Homework 5

## Assignment

Answer the following questions. You have to show codes of every step to
get credits not just an answer itself.

- Create a `.ipynb` file and start writing your answers in it.
- You must clearly specify question numbers using **_markdown_** in your file.
- Name your file as `HW5_<LASTNAME>.ipynb`, e.g., `HW5_CHEN.ipynb`.
- Submit a presentation, e.g., `HW5_CHEN.mp4` (< 5 minutes) as well.

## 1. `numpy` Questions

### <span>**<font color='royalblue'>Q. 1-1</font>**</span>

Describe your answer to the question: "_what is NumPy_?"
in a short paragraph (2-4 sentences).

### <span>**<font color='royalblue'>Q. 1-2</font>**</span>

Import numpy in your script (recall the convention).

### <span>**<font color='royalblue'>Q. 1-3</font>**</span>

Using `numpy` functions exclusively, create a `numpy.ndarray` that contains
even numbers between 0 and 9.

### <span>**<font color='royalblue'>Q. 1-4</font>**</span>

Using `numpy` functions exclusively, create a sequence of numbers with **0.5**
constant increment between 0 and 50 (i.e., 0, 0.5, 1, 1.5, ..., 49.5, 50).

### <span>**<font color='royalblue'>Q. 1-5</font>**</span>

Create a **4x4** 2-d array of **random** numbers from a _uniform distribution_
within the range of `[0, 1)`.

### <span>**<font color='royalblue'>Q. 1-6</font>**</span>

1. Import `arcpy` and set up _workspace_ as the **class geodatabase**, i.e.,
   `class_data.gdb`.
2. Create a variable that references the `crash` feature class. 

### <span>**<font color='royalblue'>Q. 1-7</font>**</span>

1. Retrieve and print out all the field names (as a `list`) in the `crash`
   feature class.
2. Convert the `crash` feature class to a (_Structured_) NumPy array with the
   following fields.
   ```python
   crash_fields = ['City', 'Crash_Type', 'Vehicles', 'Non_Motorists', 
                   'Fatalities', 'Injuries', 'Alcohol_Related',
                   'Distraction_Related', 'Drug_Related', 'Estimated_Damages',
                   'Weather_Condition', 'Light_Condition', 'Crash_Severity',
                   'Manner_of_Collision', 'Type_of_Intersection', 'Passengers',
                   'Bicyclists', 'Pedestrians', 'Citations',
                   'Property_Dmg_Amt','Vehicle_Dmg_Amt']
   ```
3. Store the structured array with a variable named: `crash_arr`.
4. Find out and **print** how many records (rows) in `crash_arr`.

### <span>**<font color='royalblue'>Q. 1-8</font>**</span>

1. Retrieve the first 7 elements of `crash_arr`.
2. Grab (retrieve and store as a variable) the first, fourth, eighth, 12th,
   50th, 100th row of the array.
3. Grab column `Fatalities` from the array.

### <span>**<font color='royalblue'>Q. 1-9</font>**</span>

Write codes to answer following codes:

1. How many crashes have **positive fatalities** in this dataset?
2. What is the **maximum** value of fatalities in the data?
3. How many **total fatalities** in the dataset?

### <span>**<font color='royalblue'>Q. 1-10</font>**</span>

1. The **total Damage** to an accident is considered as _property damage_ plus
   _vehicle damage_. Create a new array that adds the two corresponding
   columns.
2. What is the average value (`mean`) of total damage per crash?
   What about the standard deviation?
3. Find out which accident has the **maximum** _total damage_ in this dataset 
   - what was the **_weather condition_** and
   - which **_city_** did it occur?

## 2. `pandas` Questions

### <span>**<font color='royalblue'>Q. 2-1</font>**</span>

Describe your answer to the question: "what is Pandas?"
in a short paragraph (2-4 sentences).

### <span>**<font color='royalblue'>Q. 2-2</font>**</span>

import both `numpy` and `pandas` (recall the convention)

### <span>**<font color='royalblue'>Q. 2-3</font>**</span>

Convert the **total damage** from a `numpy.ndarray` cto a `pandas.Series`.

### <span>**<font color='royalblue'>Q. 2-4</font>**</span>

1. Convert `crash_arr` array to a `DataFrame` and name it `crash_df`.
2. Preview the first 5 elements.
3. Preview the last 8 elements.

### <span>**<font color='royalblue'>Q. 2-5</font>**</span>

1. Retrieve columns `['Alcohol_Related', 'Drug_Related', 'Injuries']` from
   `crash_df`
   1. using label indexing.
   2. using position-based indexing.
2. Assign these columns to a new dataframe variable (call it a name of your
   choice).
3. How many crashes are **alcohol related**? How about **drug related**?
4. Driving Under Impact (DUI) is a criminal (not civil) charge (up to 6 months
   in jail first caught). Both drug or alcohol exceeding certain limit are
   considered DUI. In this dataset, what is the **percentage** of DUI-related
   crashes?

### <span>**<font color='royalblue'>Q. 2-6</font>**</span>

1. Aggregate `crash_df` by "**City**" and then calculate the **sum**?
2. Which **city** has the largest number of citations?

### <span>**<font color='royalblue'>Q. 2-7</font>**</span>

1. Aggregate `crash_df` by "**Alcohol_Related**" and then calculate the `mean`
   for "**Estimated_Damages**"?
2. What do you find out?
3. Aggregate `crash_df` by "**Drug_Related**" and then calculated the `mean`
   for "**Estimated_Damages**"?
4. What do you find out?
5. Was Drug-related or Alcohol-related crashes cost more damage?
6. Was alcohol-related crash or drug-related crash more fatal?
   How many people were dead (per 100 crashes) for each category?
   (write codes)