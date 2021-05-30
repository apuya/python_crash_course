# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/21/2021
#
# Chapter 3: Introducing Lists
#
# Exercise 3.5 Changing Guest List:
#   You just heard that one of your guests can’t make the dinner, so you need 
# to send out a new set of invitations. You’ll have to think of someone else to 
# invite.
#
# • Start with your program from Exercise 3-4. Add a print() call at the end of 
#   your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with 
#   the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still 
#   in your list.

# List from 3-4
invites = [
    'Sam', 
    'Jaxon', 
    'Troy',
    ]
print(invites)

# del: removes item from the list
del invites[0]
print(invites)

# append allows you to add a new element at the end of the list
invites.append('Alex')
print(invites)

message = "Hey {}, dinner Friday. Are you able to make it?"

print(message.format(invites[0]))
print(message.format(invites[1]))
print(message.format(invites[2]))