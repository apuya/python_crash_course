# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/23/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.11 My Pizzas, Your Pizzas:
#   Start with your program from Exercise 4-1 (page 56). Make a copy of the 
# list of pizzas, and call it friend_pizzas. Then, do the following:
#
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite 
#   pizzas are:, and then use a for loop to print the first list. Print the 
#   message My friend’s favorite pizzas are:, and then use a for loop to print 
#   the second list. Make sure each new pizza is stored in the appropriate list.

pizzas = [
    'cheese', 
    'greek', 
    'pepperoni',
    ]
pizzas.append('italian')

friend_pizzas = pizzas[:]
friend_pizzas.append('hawaiian')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friends favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza.title())