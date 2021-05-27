# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/26/2021
#
# Chapter 5: If Statements
#
# Exercise 5.2 More Conditional Tests:
#   You don’t have to limit the number of tests you create to ten. If you want 
# to try more comparisons, write more tests and add them to 
# conditional_tests.py. Have at least one True and one False result for each of 
# the following:
# 
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less 
#   than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

name = 'mark'
print(f"name: {name}")
print(f"name == 'mark': {name == 'mark'}") # Equality test

# Inequality test determines whether two values are not equal. Exclamation 
# poin t and equal sign != is used

print(f"name != 'peter': {name != 'peter'}") # Inequality test

# lower() method allows you to test equality of case sensitive 

name = 'Mark'
print(f"name: {name}")
print(f"name == 'mark': {name.lower() == 'mark'}") # Equality test using lower()

# Numerical test

age = 22
print(f"\nage: {age}")
print(f"age == 22: {age == 22}")
print(f"age != 2: {age != 2}")
print(f"age < 2: {age < 2}") # Less than test
print(f"age <= 2: {age <= 2}") # Less than or equal to test
print(f"age > 2: {age > 2}") # Greater than test
print(f"age >= 2: {age >= 2}") # Greater than or equal to test

juice = ['apple', 'orange', 'grape']
print(f"\n{juice}")

print(f"'apple' in juice: {'apple' in juice}") # Check item in a list using keyword
print(f"'cherry' in juice: {'cherry' in juice}")

print(f"'apple' not in juice: {'apple' not in juice}") # Check item if its not on list using keyword
print(f"'cherry' not in juice: {'cherry' not in juice}")