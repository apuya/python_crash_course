# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/21/2021
#
# Chapter 3: Introducing Lists
#
# Exercise 3.7 Shrinking Guest Lists:
# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for 
# only two guests.
#
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite 
#   only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each 
#   time you pop a name from your list, print a message to that person letting them know you’re sorry you 
#   can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to 
#   make sure you actually have an empty list at the end of your program.

# List from 3-6
invites = ['Alex', 'Sam', 'Nick', 'Jaxon', 'Troy', 'Mark']

message = "Hi everyone, it looks like the new table will not arraive on time, I can only invite two people."
print(message)

# pop(): removes an item from the list and allows you to work with the removed item

message2 = "Hey {}, I apologize for the inconvenience but I have to remove you from the invitation list."

# Remove Nick from the list
popped_invites = invites.pop(2)
print(message2.format(popped_invites))

# Remove Sam from the list
popped_invites = invites.pop(1)
print(message2.format(popped_invites))

# Remove Mark from the list
popped_invites = invites.pop(3)
print(message2.format(popped_invites))

# Remove Jaxon from the list
popped_invites = invites.pop(1)
print(message2.format(popped_invites))

print(invites)

# Message the remaining two guest on the list
message3 = "Hey {}, You are still on the list."

print(message3.format(invites[0]))
print(message3.format(invites[1]))

# Remove the remaining two from the list

del invites[0]
del invites[0]
print(invites)