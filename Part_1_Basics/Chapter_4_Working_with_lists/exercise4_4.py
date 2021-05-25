# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/23/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.4 One Million:
# Make a list of the numbers from one to one million, and then use a for loop
# to print the numbers. (If the output is taking too long, stop it by pressing 
# ctrl-C or by closing the output window.)

# list() function allows you to convert the set of numbers into a list

# Crashes VS code
numbers = list(range(1, 1000001))
print(numbers)