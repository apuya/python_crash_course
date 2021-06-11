# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 06/10/2021
#
# Chapter 8: Functions
#
# Exercise 8.15 Printing Models:
#   Put the functions for the example printing_models.py in a separate file 
# called printing_functions.py. Write an import statement at the top of 
# printing_models.py, and modify the file to use the imported functions.

import printing_functions as printf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printf.print_models(unprinted_designs, completed_models)
printf.show_completed_models(completed_models)