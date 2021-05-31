# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/30/2021
#
# Chapter 8: Functions
#
# Exercise 8.9 Messages:
#   Make a list containing a series of short text messages. Pass the list to a 
# function called show_messages(), which prints each text message.

text = [
    "Hello!",
    "How are you?",
    "What did you learn today?",
    "Python",
    ]
    
def show_messages(messages):
    """
    Print series of short text messages from list.
    """
    for message in messages:
        print(message)

show_messages(text)