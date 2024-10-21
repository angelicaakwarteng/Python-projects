#!/usr/bin/env python
# coding: utf-8

# # Project - Defining Functions
# 
# This python script is a project to illustrate how a user can define their own functions for later use in the program.
# - Project layout has questions to interact with users to understand the functions defined.
# - Every function has comments for user readability.

# ### Q1
# 
# Define a python function that calculate the perimeter of the rectangle
# 
# Formular
# 
# formular => 2 X length + 2 X Width

# In[1]:


def calculate_rectangle_perimeter(length: float, width: float) -> float:
    """
    Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive.")
    
    perimeter = 2 * (length + width)
    return perimeter


# ### Q2
# Define the function to calculate the area of a circle. Round the answer to 3 decimal places.
# 
# **Preamble**
#  - Take pi as 22/7
#  - formular pi x r ** 2

# In[ ]:


import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle, rounded to 3 decimal places.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")

    # Using 22/7 for pi
    pi = 22/7
    
    # Alternative: Using math.pi for higher precision
    # pi = math.pi
    
    area = pi * (radius ** 2)
    return round(area, 3)


# ### Q3
# Define a function that takes a list of numbers and print out the **mean**, **median** and **mode**.
# 
# - Test your function with the list b
# 
# `b = [2,3,4,6,7,3,4,3,2,1,3]`

# In[ ]:


import statistics

def calculate_statistics(numbers):
    """
    Calculate and print the mean, median and mode of a list of numbers.

    Args:
        numbers (list): A list of numbers.
    """
    if not numbers:
        raise ValueError("Input list is empty.")

    mean_value = statistics.mean(numbers)
    median_value = statistics.median(numbers)
    mode_value = statistics.mode(numbers)

    print(f"Mean: {mean_value:.2f}")
    print(f"Median: {median_value}")
    print(f"Mode: {mode_value}")

# Test the function
b = [2, 3, 4, 6, 7, 3, 4, 3, 2, 1, 3]
calculate_statistics(b)


# ### Q4
# Define a function that prints out the list of the first 20 prime numbers

# In[2]:


def print_prime_numbers(n):
    """
    Print the first 'n' prime numbers.

    Args:
        n (int): Number of prime numbers to print.
    """
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    num = 2

    while prime_count < n:
        if is_prime(num):
            print(num)
            prime_count += 1
        num += 1

# Print the first 20 prime numbers
print_prime_numbers(20)


# #### Q5
# Define a function that takes a list of strings and print out the string and the length of the string.
# 
# **Example of expected output**
# 
# {"Kofi":4,
# "Ama":3,
# "Sedem":5}

# In[ ]:


def print_string_lengths(strings):
    """
    Print the length of each string in the input list.

    Args:
        strings (list): List of strings.

    Returns:
        dict: Dictionary with strings as keys and lengths as values.
    """
    string_lengths = {string: len(string) for string in strings}
    print(string_lengths)
    return string_lengths


# ### Q6
# Define a function that takes a list of strings and numbers and print out only the strings and the position of the strings.
# 
# **Preamble**
# 
# names = ['sedem', 'Kofi', 'kobla']
# 
# **Expected Output**
# 
# {'sedem': P0, 'Kofi': P1, 'kobla': P2}

# In[ ]:


def print_string_positions(mixed_list):
    """
    Print the strings and their positions in the input list.

    Args:
        mixed_list (list): List containing strings and numbers.

    Returns:
        dict: Dictionary with strings as keys and positions as values.
    """
    string_positions = {}
    for i, item in enumerate(mixed_list):
        if isinstance(item, str):
            string_positions[item] = f"P{i}"
    print(string_positions)
    return string_positions


# ### Q7
# Define a function that returns whether the sum of a person age and person's date of birth equals 2023
# 
# **Preamble**
# 
# 2001 + 22 => True
# 
# 2002 + 5 => False

# In[ ]:


def check_sum_birth_year_age(birth_year, age):
    """
    Check if the sum of birth year and age equals 2023.

    Args:
        birth_year (int): Person's birth year.
        age (int): Person's age.

    Returns:
        bool: True if sum equals 2023, False otherwise.
    """
    return birth_year + age == 2023



# ### Q8
# Define a function that determine whether a particular year is a **decade**, the output should be a boolean (True or False)
# 

# In[ ]:


def is_decade(year):
    """
    Check if a year is a decade.

    Args:
        year (int): Year to check.

    Returns:
        bool: True if year is a decade, False otherwise.
    """
    return year % 10 == 0


# ### Q9
# Define a function that contains a list of strings and punctuations,the output should on return the list of punctuations.
# 

# In[ ]:


import string

def extract_punctuations(input_list):
    """
    Extract punctuations from a list of strings.

    Args:
        input_list (list): List of strings.

    Returns:
        list: List of punctuations.
    """
    punctuations = []
    for text in input_list:
        for char in text:
            if char in string.punctuation:
                punctuations.append(char)
    return punctuations


# ### Q10
# 
# Define a lambda function that print out the cubic root of a list of numbers

# In[ ]:


import math

cubic_root = lambda numbers: [round(math.pow(num, 1/3), 3) for num in numbers]

numbers = [27, 64, 125, 216, 343]
print(cubic_root(numbers))


Output:


[3.0, 4.0, 5.0, 6.0, 7.0]


# ### Q11
# Define a lambda function that print out the cube of a list of numbers

# In[ ]:


cube = lambda numbers: [num ** 3 for num in numbers]

numbers = [1, 2, 3, 4, 5]
print(cube(numbers))


# ### Q12
# Define a function that take a list of list of numbers and return a list that contains the average of each sublist using map.

# In[ ]:


def average_sublists(lists):
    """
    Calculate the average of each sublist.

    Args:
        lists (list): List of lists containing numbers.

    Returns:
        list: List of averages.
    """
    averages = list(map(lambda sublist: sum(sublist) / len(sublist), lists))
    return averages

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(average_sublists(numbers))


# ### Q13
# Define a function that takes a list of strings and filter out strings that are upper case.

# In[3]:


def filter_uppercase(strings):
    """
    Filter out strings that are entirely uppercase.

    Args:
        strings (list): List of strings.

    Returns:
        list: List of strings that are not entirely uppercase.
    """
    return [s for s in strings if not s.isupper()]


# ### Q14
# Define a function that takes a list of numbers and print out the numbers which are prime in the list.

# In[ ]:


def print_primes(numbers):
    """
    Print prime numbers from the input list.

    Args:
        numbers (list): List of integers.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = [num for num in numbers if is_prime(num)]
    print(prime_numbers)


# ### Q15
# Define a function that take a list of strings and return a zip of each string and length of a string.

# In[ ]:


def zip_string_length(strings):
    """
    Zip each string with its length.

    Args:
        strings (list): List of strings.

    Returns:
        list: List of tuples containing string and length.
    """
    return list(zip(strings, map(len, strings)))


# ### Q16
# Define a function that takes in a number and return the first 12 multiples of the the number.
# 
# Expected Output
# 
# 2 X 1 = 2
# 
# to
# 
# 2 X 12 = 24

# In[ ]:


def multiples(n):
    """
    Generate the first 12 multiples of a number.

    Args:
        n (int): Input number.

    Returns:
        list: List of multiples.
    """
    return [f"{n} x {i} = {n * i}" for i in range(1, 13)]


# ### Q17
# Write a Python function to find the maximum of three numbers.
# 
# **Do not use the max function**

# In[ ]:


def find_max(a, b, c):
    """
    Find the maximum of three numbers.

    Args:
        a (int): First number.
        b (int): Second number.
        c (int): Third number.

    Returns:
        int: Maximum number.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# ### Q18
# Write a Python function to multiply all the numbers in a list.

# In[ ]:


Using For Loop

def multiply_numbers(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


Using Lambda Function

multiply_numbers = lambda numbers: eval('*'.join(map(str, numbers)))



# ### Q19
# Write a Python program to reverse a string

# In[ ]:


Lambda Function
reverse_string = lambda s: s[::-1]

# Example usage:
input_str = "Hello World"
reversed_str = reverse_string(input_str)
print(reversed_str)  # Output: "dlroW olleH"

Method 1: Slicing


def reverse_string(s):
    return s[::-1]

# Example usage:
input_str = "Hello World"
reversed_str = reverse_string(input_str)
print(reversed_str)  # Output: "dlroW olleH"


Method 2: Reversed Function


def reverse_string(s):
    return "".join(reversed(s))

# Example usage:
input_str = "Hello World"
reversed_str = reverse_string(input_str)
print(reversed_str)  # Output: "dlroW olleH"


# ### Q20
# Write a python function to return the length of a string.

# In[ ]:


Here are multiple Python methods to return the length of a string:


Method 1: Lambda Function


string_length = lambda s: len(s)

# Example usage:
input_str = "Hello World"
length = string_length(input_str)
print(length)  # Output: 11


Method 2: Built-in Len Function


def string_length(s):
    return len(s)

# Example usage:
input_str = "Hello World"
length = string_length(input_str)
print(length)  # Output: 11


Method 3: Looping


def string_length(s):
    length = 0
    for char in s:
        length += 1
    return length

# Example usage:
input_str = "Hello World"
length = string_length(input_str)
print(length)  # Output: 11


# Have a lovely coding weekend
