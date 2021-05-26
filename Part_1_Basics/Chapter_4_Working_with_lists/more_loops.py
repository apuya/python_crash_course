# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/23/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.12 More Loops:
#   All versions of foods.py in this section have avoided using for loops when 
# printing to save space. Choose a version of foods.py, and write two for loops
# to print each list of foods.

# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)