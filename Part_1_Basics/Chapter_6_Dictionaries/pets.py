# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.8 Pets:
#    Make several dictionaries, where each dictionary represents a different 
# pet. In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list 
# and as you do, print everything you know about each pet.

pets = []

pet_0 = {
    'name': 'theo',
    'kind': 'dog',
    'owner': 'mark'
    }

pet_1 = {
    'name': 'perry',
    'kind': 'pariot',
    'owner': 'sam'
    }

pet_2 = {
    'name': 'trip',
    'kind': 'dog',
    'owner': 'troy'
    }

pets.append(pet_0)
pets.append(pet_1)
pets.append(pet_2)

for pet in pets:
    print("\nPet info:")
    for key, value in pet.items():
        print(f"{key}: {value}")