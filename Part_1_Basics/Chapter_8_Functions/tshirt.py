# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 8: Functions
#
# Exercise 8.3 T-Shirt:
#   Write a function called make_shirt() that accepts a size and the text of a 
# message that should be printed on the shirt. The function should print a 
# sentence summarizing the size of the shirt and the message printed on it. 
#   Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments.

def make_shirt(shirt_size, message_printed):
    """
    Display shirt specifications.
    """
    print(f"\nThe size of the shirt will be: {shirt_size}.")
    print(f'"{message_printed}" will be printed on the shirt.')

make_shirt('medium', 'Hello World!')
make_shirt(message_printed = "Python", shirt_size = "small")