# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/12/2021
#
# Chapter 9: Classes
#
# Exercise 9.2 Three Restaurants:
#   Start with your class from Exercise 9-1. Create three different instances 
# from the class, and call describe_restaurant() for each instance.

class Restaurant:
    """
    Restaurant information.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize restuarant name and cuisine type.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """
        Prints restaurant information.
        """
        print(f"\n{self.restaurant_name} serves {self.cuisine_type} cuisine")

    def open_restaurant(self):
        """
        Prints that the restaurant is open.
        """
        print(f"\n{self.restaurant_name} is open.")

restaurant_1 = Restaurant('Olive Garden', 'Italian') 
restaurant_2 = Restaurant('Nobu', 'Japanese')
restaurant_3 = Restaurant('Eureka!', 'American')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()