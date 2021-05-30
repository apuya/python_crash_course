# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/24/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.13 Buffet:
#   A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
#
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
#   change.
# • The restaurant changes its menu, replacing two of the items with different 
#   foods. Add a line that rewrites the tuple, and then use a for loop to print
#   each of the items on the revised menu.

menu = (
    'pasta', 'steak', 'sushi', 
    'cake', 'shrimp',
    )
for food in menu:
    print(food)

# Tuple allows you to create a list of items that cannot change. A tuple list 
# is made by using parentheses instead of square brackets.
# Immutable are values that cannot change

# menu[0] = 'chicken' # prints out "TypeError: 'tuple' object does not support 
# item assignment"

menu = (
    'chicken', 'steak', 'crab', 
    'cake', 'shrimp',
    )
for food in menu:
    print(food)