# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/1/2021
#
# Chapter 9: Classes
#
# Exercise 9.13 Dice:
#   Make a class Die with one attribute called sides, which has a default value 
# of 6. Write a method called roll_die() that prints a random number between 1
# and the number of sides the die has. Make a 6-sided die and roll it 10 times.
#   Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint 

class Dice:
    """
    Dice that can be rolled.
    """

    def __init__(self, sides=6):
        """
        Initialize the attributes.
        """
        self.sides = sides

    def roll_dice(self):
        """
        Prints random numbers between 1 and the number of sides the dice has.
        """
        return randint(1, self.sides)

