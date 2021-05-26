# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/23/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.6 Odd Numbers:
#   Use the third argument of the range() function to make a list of the odd 
# numbers from 1 to 20. Use a for loop to print each number.

# The third argument isused as a step size
numbers = list(range(1, 20, 2))
for odd in numbers:
    print(odd)