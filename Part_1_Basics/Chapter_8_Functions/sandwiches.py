# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/30/2021
#
# Chapter 8: Functions
#
# Exercise 8.12 Sandwiches:
#   Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the 
# function call provides, and it should print a summary of the sandwich that’s 
# being ordered. Call the function three times, using a different number of 
# arguments each time.

def sandwich_order(*fillings):
    """
    Collects as many item, and prints out the items.
    """
    print("\nItems in sandwich:")
    for filling in fillings:
        print(filling.title())

sandwich_order(
    'tomato', 'lettuce', 
    'bacon', 'cheese',
    )
sandwich_order(
    'grilled chicken', 'cheddar cheese', 
    'lettuce', 'tomato',
    )
sandwich_order(
    'chedder cheese', 'swiss cheese', 
    'american cheese', 'Provolone cheese',
    )