# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/12/2021
#
# Chapter 9: Classes
#
# Exercise 9.3 Users:
#   Make a class called User. Create two attributes called first_name and 
# last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that 
# prints a personalized greeting to the user. 
#   Create several instances representing different users, and call both 
# methods for each user.

class User:
    """
    Simple user profile.
    """

    def __init__(self, first_name, last_name, age, email):
        """
        Initialize attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """
        Prints a summary of the user's information.
        """
        print(f"\nFirst Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """
        Prints personalized greeting to the user.
        """
        print(f"\nHello {self.first_name.title()}! You are currently logged in.")

user_0 = User('test', 'user', '22', 'testuser@email.com')
user_1 = User('mark', 'apuya', '25', 'contact@mapuya.com')

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()