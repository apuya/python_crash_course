# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.1 Person:
#   Use a dictionary to store information about a person you know. Store their 
# first name, last name, age, and the city in which they live. You should have
# keys such as first_name, last_name, age, and city. Print each piece of
# information stored in your dictionary.

# Dictionary is a collection of key-value pairs. A key is connected to a value.
# The key is used to access the value.

user_0 = {
    'first_name': 'mark', 
    'last_name': 'apuya', 
    'age': 25, 
    'city': 'honolulu'
    }

print(user_0['first_name'])
print(user_0['last_name'])
print(user_0['age'])
print(user_0['city'])