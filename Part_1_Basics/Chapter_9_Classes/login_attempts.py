# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/12/2021
#
# Chapter 9: Classes
#
# Exercise 9.5 Login Attempts:
#   Add an attribute called login_attempts to your User class from Exercise 9-3
# (page 162). Write a method called increment_login_attempts() that increments 
# the value of login_attempts by 1. Write another method called 
# reset_login_attempts() that resets the value of login_attempts to 0.
#   Make an instance of the User class and call increment_login_attempts() 
# several times. Print the value of login_attempts to make sure it was 
# incremented properly, and then call reset_login_attempts(). Print 
# login_attempts again to make sure it was reset to 0.

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
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """
        Increment login attempt.
        """
        self.login_attempts += 1

    def reset_login_attempt(self):
        """
        Reset login attempt to 0.
        """
        self.login_attempts = 0

user_0 = User('mark', 'apuya', '25', 'contact@mapuya.com')
user_0.describe_user()
user_0.greet_user()

user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(f"\n{user_0.first_name.title()}'s login attempts: " + str(user_0.login_attempts))

user_0.reset_login_attempt()
print(f"\nLogin attempt has been reset to: " + str(user_0.login_attempts))