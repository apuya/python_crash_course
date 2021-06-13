# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/12/2021
#
# Chapter 9: Classes
#
# Exercise 9.4 Number Served:
#   Start with your program from Exercise 9-1 (page 162). Add an attribute 
# called number_served with a default value of 0. Create an instance called
# restaurant from this class. Print the number of customers the restaurant has 
# served, and then change this value and print it again.
#   Add a method called set_number_served() that lets you set the number of 
# customers that have been served. Call this method with a new number and print
# the value again.
#   Add a method called increment_number_served() that lets you increment the 
# number of customers who’ve been served. Call this method with any number you 
# like that could represent how many customers were served in, say, a day of 
# business.

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

    def discribe_restaurant(self):
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

restaurant = Restaurant('Olive Garden', 'Italian') 
restaurant.discribe_restaurant()
print(f"\nNumber served: {restaurant.number_served}")

restaurant.number_served = 22
print(f"\nNumber served: {restaurant.number_served}")

restaurant.set_number_served(20)
print(f"\nNumber served: {restaurant.number_served}")

restaurant.increment_number_served(2)
print(f"\nNumber served: {restaurant.number_served}")