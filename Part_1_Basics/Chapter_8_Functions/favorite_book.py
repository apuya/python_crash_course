# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 8: Functions
#
# Exercise 8.2 Favorite Book:
#   Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as One of my favorite books is 
# Alice in Wonderland. Call the function, making sure to include a book title 
# as an argument in the function call.

def favorite_book(title):
    """
    Display favorite book.
    Accepts one parameter.
    """
    print(f'My favorite book is "{title.title()}".')

favorite_book('the 48 laws of power')