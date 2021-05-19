# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date:
#
# Chapter 16: Downloading Data
#
# Exercise 16.6 Refactoring:
# The loop that pulls data from all_eq_dicts uses variables for the magnitude, longitude, latitude, and title of each earthquake 
# before append- ing these values to their appropriate lists. This approach was chosen for clar- ity in how to pull data from a 
# JSON file, but it’s not necessary in your code. Instead of using these temporary variables, pull each value from eq_dict and 
# append it to the appropriate list in one line. Doing so should shorten the body of this loop to just four lines.