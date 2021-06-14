# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/13/2021
#
# Chapter 9: Classes
#
# Exercise 9.7 Admin:
#   An administrator is a special kind of user. Write a class called Admin that
# inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise
# 9-5 (page 167). Add an attribute, privileges, that stores a list of strings 
# like "can add post", "can delete post", "can ban user", and so on. Write a 
# method called show_privileges() that lists the administrator’s set of 
# privileges. Create an instance of Admin, and call your method. 

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

class Admin(User):
    """
    Admin for user information.
    """

    def __init__(self, first_name, last_name, age, email):
        """
        Initialize Attributes.
        """
        super().__init__(first_name, last_name, age, email)
        self.privileges = []

    def show_privileges(self):
        """
        Displays privileges of admin.
        """
        print("\nPrivileges of the admin:")
        for privilege in self.privileges:
            print(privilege.title())

marka = Admin('mark', 'apuya', '25', 'contact@mapuya.com')
marka.describe_user()
marka.greet_user()

marka.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]
marka.show_privileges()