# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 7: User Input and While Loops
#
# Exercise 7.1 Restaurant Seating:
#   Write a program that asks the user how many people are in their dinner 
# group. If the answer is more than eight, print a message saying they’ll have 
# to wait for a table. Otherwise, report that their table is ready.

message = input("How many people are in yout group? ")
guest = int(message)

if guest > 8:
    print("\nThere is a little wait for the table.")
else: 
    print("\nPerfect, we have a table ready for you guys.")