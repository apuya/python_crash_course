# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/23/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.10 Slices:
#   Using one of the programs you wrote in this chapter, add several lines to 
# the end of the program that do the following:
#
# • Print the message The first three items in the list are:. Then use a slice 
#   to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Use a slice
#   to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Use a slice to 
#   print the last three items in the list.

# Program from 4-9
cubed = [value ** 3 for value in range(1, 11)]
print(cubed)

# Slicing allows you to work with specific items in the list

print(f"The first three items in the list are: {cubed[0:3]}")
print(f"Three items from the middle of the list are: {cubed[4:7]}")
print(f"The last three items in the list are: {cubed[7:11]}")