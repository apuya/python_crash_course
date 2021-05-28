# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 5: If Statements
#
# Exercise 5.10 Checking Username:
#   Do the following to create a program that simulates how websites ensure 
# that everyone has a unique username.
#
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or two 
#   of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already 
#   been used. If it has, print a message that the person will need to enter a 
#   new username. If a username has not been used, print a message saying that 
#   the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used, 
#   'JOHN' should not be accepted. (To do this, you’ll need to make a copy 
#   of current_users containing the lowercase versions of all existing users.)

current_users = ['mark', 'alex', 'troy', 'sam', 'jaxon']
new_users = ['jaxon', 'troy', 'carl', 'john', 'jose']

for new_user in new_users:
    if new_user in current_users:
        print(f"The useraname {new_user.title()} is already taken, please" 
               " eneter a new username.")
    else:
        print(f"The username {new_user.title()} is available.")