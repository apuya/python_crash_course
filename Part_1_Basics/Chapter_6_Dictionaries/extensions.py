# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.12 Extensions:
#   We’re now working with examples that are complex enough that they can be 
# extended in any number of ways. Use one of the example programs from this 
# chapter, and extend it by adding new keys and values, changing the context of 
# the program or improving the formatting of the output.

# favorite_languages.py

favorite_languages = {
    'jen': {
       'languages': ['python', 'ruby'],
       'years': 5
        } ,
    'sarah': {
        'languages': ['c'],
        'years': 2
        },
    'edward': {
        'languages': ['ruby', 'go'],
        'years': 3
        },
    'phil': {
        'languages': ['python', 'haskell'],
        'years': 6
        }
    }

for name, info in favorite_languages.items():
    print(f"\n{name.title()} has {info['years']} years of coding." )
    print(f"{name.title()} favorite languages are:")

    for language in info['languages']:
        print(f"{language.title()}")