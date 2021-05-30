# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 7: User Input and While Loops
#
# Exercise 7.9 No Pastrami:
#   Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 
# 'pastrami' appears in the list at least three times. Add code near the 
# beginning of your program to print a message saying the deli has run out of 
# pastrami, and then use a while loop to remove all occurrences of 'pastrami' 
# from sandwich_orders. Make sure no pastrami sandwiches end up in 
# finished_sandwiches.

sandwich_orders = [
    'pastrami', 'chicken', 'blt',
    'pastrami', 'grilled cheese', 
    'ham and cheese', 'pastrami'
    ]
finished_sandwich = []

print("The deli has run out of pastrami for the day.\n")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich != 'pastrami':
        print(f"I am currently making {current_sandwich} sandwich.")
        finished_sandwich.append(current_sandwich)

print("\nHere are the completed sandwiches:")
for sandwich in finished_sandwich:
    print(sandwich.title())