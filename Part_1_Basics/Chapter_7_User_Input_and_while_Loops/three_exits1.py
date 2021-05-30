# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 7: User Input and While Loops
#
# Exercise 7.6 Three Exits:
#   Write different versions of either Exercise 7-4 or Exercise 7-5 that do 
# each of the following at least once:
#
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

# Conditional test
# puzza_topping.py
message = "\nWhat toppings would you like on your pizza?"
message += "\nEnte 'quite' to end the program. "

toppings = ""

while toppings != 'quit':
   toppings = input(message)

   if message != 'quit':
       print(toppings)