# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.7 People:
#   Start with the program you wrote for Exercise 6-1 (page 99). Make two new 
# dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop 
# through the list, print everything you know about each person.

people = []

user_0 = {
    'first_name': 'mark', 
    'last_name': 'apuya', 
    'age': 25, 
    'city': 'honolulu'
    }
people.append(user_0)

user_1 = {
    'first_name': 'troy', 
    'last_name': 'cruz', 
    'age': 24, 
    'city': 'Los Angeles'
    }
people.append(user_1)

user_2 = {
    'first_name': 'sam', 
    'last_name': 'brown', 
    'age': 22, 
    'city': 'santa cruz'
    }
people.append(user_2)

for person in people:
    first = person['first_name'].title()
    last = person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(f"{first} {last} is {age}, from {city}.")