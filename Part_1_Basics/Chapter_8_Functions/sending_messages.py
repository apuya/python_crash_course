# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/30/2021
#
# Chapter 8: Functions
#
# Exercise 8.10 Sending Messages:
#   Start with a copy of your program from Exercise 8-9. Write a function 
# called send_messages() that prints each text message and moves each message 
# to a new list called sent_messages as it’s printed. After calling the 
# function, print both of your lists to make sure the messages were moved 
# correctly.

text = [
    "Hello!",
    "How are you?",
    "What did you learn today?",
    "Python",
    ]
sent_messages = []

def send_messages(messages, sent_messages):
    """
    Print messages, and move each message to a new list.
    """
    print("\nSent Messages: ")
    while messages:
        current_messages = messages.pop()
        print(current_messages)
        sent_messages.append(current_messages)

def show_messages(messages):
    """
    Print series of short text messages from list.
    """
    print("\nMessages:")
    for message in messages:
        print(message)

show_messages(text)
send_messages(text, sent_messages)

print("\nLists:")
print(f"text: {text}")
print(f"sent_messages: {sent_messages}")