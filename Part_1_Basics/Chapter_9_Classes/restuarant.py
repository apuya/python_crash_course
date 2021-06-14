# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/11/2021
#
# Chapter 9: Classes
#
# Exercise 9.1 Restuarant:
#   Make a class called Restaurant. The __init__() method for Restaurant should 
# store two attributes: a restaurant_name and a cuisine_type. Make a method 
# called describe_restaurant() that prints these two pieces of information, and 
# a method called open_restaurant() that prints a message indicating that the 
# restaurant is open.
#   Make an instance called restaurant from your class. Print the two 
# attributes individually, and then call both methods.

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

restaurant = Restaurant('Olive Garden', 'Italian') 
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()