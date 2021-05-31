# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/30/2021
#
# Chapter 8: Functions
#
# Exercise 8.11 Archived Messages:
#   Start with your work from Exercise 8-10. Call the function send_messages() 
# with a copy of the list of messages. After calling the function, print both 
# of your lists to show that the original list has retained its messages.

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
send_messages(text[:], sent_messages)

print("\nLists:")
print(f"text: {text}")
print(f"sent_messages: {sent_messages}")