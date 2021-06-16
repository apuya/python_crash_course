# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/14/2021
#
# Chapter 9: Classes
#
# Exercise 9.10 Imported Restaurant:
#   Using your latest Restaurant class, store it in a module. Make a separate
# file that imports Restaurant. Make a Restaurant instance, and call one of 
# Restaurant’s methods to show that the import statement is working properly.

from ice_cream_stand import IceCreamStand

salt_and_straw = IceCreamStand('Salt and Straw')
salt_and_straw.flavors = ['lavender honey', 'chocolate', 'coffee']

salt_and_straw.describe_restaurant()
salt_and_straw.display_flavors()