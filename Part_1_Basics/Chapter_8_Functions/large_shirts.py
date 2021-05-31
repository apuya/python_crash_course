# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 8: Functions
#
# Exercise 8.4 Large Shirts:
#   Modify the make_shirt() function so that shirts are large by default with a 
# message that reads I love Python. Make a large shirt and a medium shirt with 
# the default message, and a shirt of any size with a different message.

def make_shirt(shirt_size='large', message_printed='I Love Python'):
    """
    Display shirt specifications.
    """
    print(f"\nThe size of the shirt will be: {shirt_size}.")
    print(f'"{message_printed}" will be printed on the shirt.')

make_shirt()
make_shirt('medium')
make_shirt(message_printed="Python", shirt_size="small")