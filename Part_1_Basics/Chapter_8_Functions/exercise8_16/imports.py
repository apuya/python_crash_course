# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/11/2021
#
# Chapter 8: Functions
#
# Exercise 8.16 Imports:
#   Using a program you wrote that has one function in it, store that function 
# in a separate file. Import the function into your main program file, and call 
# the function using each of these approaches:
#
# import module_name
# from module_name import function_name
# from module_name import function_name as fn 
# import module_name as mn
# from module_name import *

import album
print(album.make_album('Pink Sweat$', "At My Worst"))

from album import make_album
print(make_album('Kane Brown', 'Worship You'))

from album import make_album as ma
print(ma('Meduza', 'Paradise'))

import album as a
print(a.make_album('Pink Sweat$', 'At My Worst'))

from album import *
print(make_album('Kane Brown', 'Worship You'))