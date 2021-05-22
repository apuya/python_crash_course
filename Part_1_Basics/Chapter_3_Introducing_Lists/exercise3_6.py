# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/21/2021
#
# Chapter 3: Introducing Lists
#
# Exercise 3.6 More Guests:
# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing 
#   people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

# List from exercise 3-5
invites = ['Sam', 'Jaxon', 'Troy']
print(invites)

# Insert new guest at the beginning of the list using insert()
invites.insert(0, 'Alex')

# Insert new guest at the middle of the list using insert()
invites.insert(2, 'Nick')

# Insert new guest at the end of the list by using append()
invites.append('Mark')

# List with new guest
print(invites)

# New invite message
message1 = "Hey {}, I am planning a dinner this friday, will you be able to come?"

print(message1.format(invites[0]))
print(message1.format(invites[1]))
print(message1.format(invites[2]))
print(message1.format(invites[3]))
print(message1.format(invites[4]))

# Inform invites that I found a bigger table
message2 = "Hey everyone, I got a bigger table to accomodate all of us."
print(message2)
