# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/27/2021
#
# Chapter 5: If Statements
#
# Exercise 5.7 Favorite Fruit:
#   Make a list of your favorite fruits, and then write a series of independent 
# if statements that check for certain fruits in your list.
#
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit 
#   is in your list. If the fruit is in your list, the if block should print a 
#   statement, such as You really like bananas!

favorite_fruits = ['banana', 'blueberry', 'strawberry']
print(f"Favorite fruits: {favorite_fruits}")

if 'banana' in favorite_fruits:
    print("Bananas are my favorite!")
if 'orange' in favorite_fruits:
    print("Orange are my favorite!")
if 'strawberry' in favorite_fruits:
    print("strawberry are my favorite!")
if 'blueberry' in favorite_fruits:
    print("Blueberry are my favorite!")
if 'grapes' in favorite_fruits:
    print("Grapes are my favorite!")