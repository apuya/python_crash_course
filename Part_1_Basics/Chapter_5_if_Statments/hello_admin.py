# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/27/2021
#
# Chapter 5: If Statements
#
# Exercise 5.8 Hello Admin:
#   Make a list of five or more usernames, including the name 'admin'. Imagine  
# you are writing code that will print a greeting to each user after they log 
# in to a website. Loop through the list, and print a greeting to each user:
#
# • If the username is 'admin', print a special greeting, such as Hello admin, 
#   would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for 
#   logging in again.

usernames = [
    'admin', 'mark', 'jaxon', 
    'troy', 'alex',
    ]

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see the status report?")
    else:
        print("Hello " + user.title() + ", you are currently logged in")