# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 7: User Input and While Loops
#
# Exercise 7.3 Multiples of Ten:
#    Ask the user for a number, and then report whether the number is a 
# multiple of 10 or not.

# % modulo operattor divides the number by another number and returns the 
# remainder.

message = input("Please enter a number: ")
number = int(message)

# modulo operator is used to determin if the input number is a multiple of 10. 
# If the remainder is = 0 then it is a multiple of 10 
remainder = number % 10 

if remainder == 0:
    print(f"{number} is a multiple of 10.")
else: 
    print(f"{number} is not a multiple of 10.")