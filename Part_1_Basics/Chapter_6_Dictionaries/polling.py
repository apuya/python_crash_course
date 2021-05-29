# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.6 Polling:
# Use the code in favorite_languages.py (page 97).
# 
# • Make a list of people who should take the favorite languages poll. Include 
#   some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have 
#   already taken the poll, print a message thanking them for responding. If 
#   they have not yet taken the poll, print a message inviting them to take the 
#   poll.

# favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is " 
          f"{language.title()} .")

poll = ['jaxon', 'troy', 'alex', 'sam', 'sarah', 'jen', 'mark']
for people in poll:
    if people in favorite_languages.keys():
        print(f"Thank you for taking the poll, {people.title()}!")
    else:
        print(f"{people.title()}, what's your favorite programming language?")