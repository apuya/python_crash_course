# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/15/2021
#
# Chapter 9: Classes
#
# Exercise 9.12 Multiple Modules:
#   Store the User class in one module, and store the Privileges and Admin 
# classes in a separate module. In a separate file, create an Admin instance
# and call show_privileges() to show that everything is still working 
# correctly.

from admin import Admin

marka = Admin('mark', 'apuya', '25', 'contact@mapuya.com')
marka.describe_user()

mark_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]
    
marka.privileges.privileges = mark_privileges
marka.privileges.show_privileges()