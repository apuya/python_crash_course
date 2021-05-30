# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 7: User Input and While Loops
#
# Exercise 7.10 Dream Vacation:
#    Write a program that polls users about their dream vaction. Write a prompt 
# similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

poll = {}

while True:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would"
                     " you go? ")

    # Stores data into dictionary.
    poll[name] = response

    repeat = input("\nWould you like another person to respond? (yes/no) ")
    if repeat == 'no':
        break

print("\nPoll Results:")
for name, response in poll.items():
    print(f"{name.title()} would like to visit {response.title()}.")