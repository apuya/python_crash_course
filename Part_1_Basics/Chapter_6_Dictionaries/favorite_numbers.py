# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.2 Favorite Numbers:
#   Use a dictionary to store people’s favorite numbers. Think of five names, 
# and use them as keys in your dictionary. Think of a favorite number for each 
# person, and store each as a value in your dictionary. Print each person’s 
# name and their favorite number. For even more fun, poll a few friends and get 
# some actual data for your program.

favorite_numbers = {
    'mark': 22,
    'jaxon': 20,
    'alex': 2,
    'sam': 30,
    'troy': 12
    }

number = favorite_numbers['mark']
print(f"Mark's favorite number is {number}.")

number = favorite_numbers['jaxon']
print(f"Jaxon's favorite number is {number}.")

number = favorite_numbers['alex']
print(f"Alex's favorite number is {number}.")

number = favorite_numbers['sam']
print(f"Sam's favorite number is {number}.")

number = favorite_numbers['troy']
print(f"Troy's favorite number is {number}.")