# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/13/2021
#
# Chapter 9: Classes
#
# Exercise 9.6 Ice Cream Stand:
#   An ice cream stand is a specific kind of restaurant. Write a class called 
# IceCreamStand that inherits from the Restaurant class you wrote in Exercise 
# 9-1 (page 162) or Exercise 9-4 (page 167). Either version of the class will
# work; just pick the one you like better. Add an attribute called flavors
# that stores a list of ice cream flavors. Write a method that displays these 
# flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
    """
    Restaurant information.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize restuarant name and cuisine type
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """
        Prints restaurant information.
        """
        print(f"\n{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        """
        Prints that the restaurant is open.
        """
        print(f"\n{self.restaurant_name} is open.")

    def set_number_served(self, number_served):
        """
        Set the number of customers served.
        """
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """
        Increment the number of customers who have been served.
        """
        self.number_served += number_served

class IceCreamStand(Restaurant):
    """
    Ice cream stand information.
    """

    def __init__(self, restaurant_name, cuisine_type = 'Ice Cream'):
        """
        Initialize attributes of the parent class.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """
        Displays flavors.
        """
        print(f"\nFlavors available at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(flavor.title())

salt_and_straw = IceCreamStand('Salt and Straw')
salt_and_straw.flavors = ['lavender honey', 'chocolate', 'coffee']

salt_and_straw.describe_restaurant()
salt_and_straw.display_flavors()