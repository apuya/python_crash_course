# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/15/2021
#
# Chapter 9: Classes
#
# Exercise 9.11 Imported Admin:
#   Start with your work from Exercise 9-8 (page 173). Store the classes User,
# Privileges, and Admin in one module. Create a separate file, make an Admin 
# instance, and call show_privileges() to show that everything is working 
# correctly.

from user import Admin

marka = Admin('mark', 'apuya', '25', 'contact@mapuya.com')
marka.describe_user()
marka.greet_user()

mark_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]
marka.privileges.privileges = mark_privileges
marka.privileges.show_privileges()