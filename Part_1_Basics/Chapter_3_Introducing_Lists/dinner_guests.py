# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/22/2021
#
# Chapter 3: Introducing Lists
#
# Exercise 3.9 Dinner Guests:
#   Working with one of the programs from Exercises 3-4 through 3-7 (page 42), 
# use len() to print a message indicating the number of people you are inviting
# to dinner.

# List from 3-6
invites = [
    'Alex', 'Sam', 
    'Nick', 'Jaxon', 
    'Troy', 'Mark',
    ]

# len(): tells you the length of the list
message = "There are {} on the invite list."
print(message.format(len(invites)))