# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 5: If Statements
#
# Exercise 5.9 No Users:
# Add an if test to hello_admin.py to make sure the list of users is not empty.
#
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
#   message is printed.

# hello_admin.py
usernames = ['admin', 'mark', 'jaxon', 'troy', 'alex']

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see the status report?")
        else:
            print("Hello " + user.title() + ", you are currently logged in")
else: 
    print("We need to find some users!")