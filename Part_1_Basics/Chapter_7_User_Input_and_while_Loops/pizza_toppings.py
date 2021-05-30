# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 7: User Input and While Loops
#
# Exercise 7.4 Pizza Toppings:
#   Write a loop that prompts the user to enter a series of pizza toppings 
# until they enter a 'quit' value. As they enter each topping, print a message 
# saying you’ll add that topping to their pizza.

# while loop is a loop that runs as long as a certain condition is true.

message = "\nWhat toppings would you like on your pizza?"
message += "\nEnte 'quite' to end the program. "

toppings = ""

while toppings != 'quit':
   toppings = input(message)

   if message != 'quit':
       print(toppings)