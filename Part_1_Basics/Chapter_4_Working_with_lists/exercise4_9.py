# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/23/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.9 Cube Comprehension:
# Use a list comprehension to generate a list of the first 10 cubes.

# List comprehenesion allows you to generate the same list in just one line of
# code

cubed = [value ** 3 for value in range(1, 11)]
print(cubed)