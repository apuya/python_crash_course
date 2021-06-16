"""
Classes modeling users.
"""

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