# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/19/2021
#
# Chapter 2: Variables and Simple Data Types
#
# Exercise 2.7 Stripping Name:
#   Use a variable to represent a person’s name, and include some whitespace 
# characters at the beginning and end of the name. Make sure you use each 
# character combination, "\t" and "\n", at least once.
#   Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip().

# whitespace: are nonprinting chracters: spaces, tabs, and end-of-line symbols

name = "Mark Lester Apuya"
print(name)

# \t: add tab to the text
name = "\tMark\tLester\tApuya"
print(name)

# \n: add a new line 
name = "Mark\nLester\nApuya"
print(name)

# Stripping functions: temprarily removes extra space from the left, right, or 
# both sides
name = " Mark Lester Apuya "
print("'" + name + "'")

# lstrip(): removes extra space on the left side
print("'" + name.lstrip() + "'")

# rstrip(): removes extra space on the right side
print("'" + name.rstrip() + "'")

# strip(): removes extra space the left and right side
print("'" + name.strip()+ "'")