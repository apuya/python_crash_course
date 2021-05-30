# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/21/2021
#
# Chapter 3: Introducing Lists
#
# Exercise 3.4 Guest List:
#   If you could invite anyone, living or deceased, to dinner, who would you 
# invite? Make a list that includes at least three people you’d like to invite 
# to dinner. Then use your list to print a message to each person, inviting 
# them to dinner.

invites = [
    'Sam', 
    'Jaxon', 
    'Troy',
    ]

message = "{}, were having dinner on friday, be there?"

print(message.format(invites[0]))
print(message.format(invites[1]))
print(message.format(invites[2]))