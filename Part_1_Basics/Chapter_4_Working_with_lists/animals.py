# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/23/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.Animals:
#   Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to print 
# out the name of each animal.
# 
# • Modify your program to print a statement about each animal, such as
#   A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in 
#   common. You could print a sentence such as Any of these animals would make 
#   a great pet!

animals = ['duck', 'chicken', 'peacock']
print(animals)

for animal in animals:
    print(animal)

for animal in animals:
    print(f"A {animal} has feathers.")

print("These animals are birds.")