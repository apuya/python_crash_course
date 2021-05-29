# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.10 Favorite Numbers:
#   Modify your program from Exercise 6-2 (page 99) so each person can have 
# more than one favorite number. Then print each person’s name along with their 
# favorite numbers.

favorite_numbers = {
    'mark': [22, 2, 20],
    'jaxon': [20, 4, 10],
    'alex': [2, 69, 14],
    'sam': [30, 23, 16],
    'troy': [12, 56, 99]
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite number:")
    for number in numbers:
        print(number)