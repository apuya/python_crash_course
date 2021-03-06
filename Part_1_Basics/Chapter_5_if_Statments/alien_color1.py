# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/26/2021
#
# Chapter 5: If Statements
#
# Exercise 5.3 Alien Color #1:
#   Imagine an alien was just shot down in a game. Create a variable called 
# alien_color and assign it a value of 'green', 'yellow', or 'red'.
#
# • Write an if statement to test whether the alien’s color is green. If it is, 
#   print a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that 
#   fails. (The version that fails will have no output.)

alien_color = 'green'
print(f"Alien color: {alien_color}")
if alien_color == 'green':              # Passes test
    print("You just earned 5 points!")

alien_color = 'red'
print(f"Alien color: {alien_color}")
if alien_color == 'green':              # Failes test                   
    print("You just earned 5 points!")