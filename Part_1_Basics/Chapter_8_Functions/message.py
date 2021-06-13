# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date:
# 05/29/2021
# Chapter 8: Functions
#
# Exercise 8.1 Message:
#   Write a function called display_message() that prints one sentence telling 
# everyone what you are learning about in this chapter. Call the function, and 
# make sure the message displays correctly.

# Functions are a block of  code that does one specific job.
# def is used to define a function.

def display_message():
    # docstring are a type of comment, It describes what the function does.
    """
    Display simple sentence.
    """  
    print("We are learning functions in this chapter.")

display_message()   # calls the function