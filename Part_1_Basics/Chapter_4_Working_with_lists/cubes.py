# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/23/2021
#
# Chapter 4: Working With Lists
#
# Exercise 4.8 Cubes:
# A number raised to the third power is called a cube. For example, the cube of 
# 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, 
# the cube of each integer from 1 through 10), and use a for loop to print out 
# the value of each cube.

# Two asterisks ** represent exponents

cubed = []
for value in range(1, 11):
    cube = value ** 3
    cubed.append(cube)

print(cubed)

for cube in cubed:
    print(cube)