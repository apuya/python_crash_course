"""
Collection of classes modeling admin.
"""

from user import User

class Admin(User):
    """
    Admin for user information.
    """

    def __init__(self, first_name, last_name, age, email):
        """
        Initialize Attributes.
        """
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()

class Privileges():
    """
    Admin privileges.
    """

    def __init__(self, privileges=[]):
        """
        Initialize attributes.
        """
        self.privileges = privileges

    def show_privileges(self):
        """
        Displays privileges of admin.
        """
        print("\nPrivileges of the admin:")
        for privilege in self.privileges:
            print(privilege.title())