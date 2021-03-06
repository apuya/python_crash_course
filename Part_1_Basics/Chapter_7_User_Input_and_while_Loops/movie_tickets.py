# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 7: User Input and While Loops
#
# Exercise 7.5 Movie Tickets:
#   A movie theater charges different ticket prices depending on a person’s 
# age. If a person is under the age of 3, the ticket is free; if they are 
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket 
# is $15. Write a loop in which you ask users their age, and then tell them the 
# cost of their movie ticket.

message = "\nHow old are you?"
message += "\nEnter 'quite' when you are finished: "

while True:
    age = input(message)
    if age == 'quit':
        break
    
    age = int(age)

    if age < 3:
        print("\tThe ticket is free.")
    elif age < 13:
        print("\tThe ticket cost $10.")
    else:
        print("\tThe ticket cost $15.")