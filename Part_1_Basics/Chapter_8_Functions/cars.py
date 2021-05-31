# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/30/2021
#
# Chapter 8: Functions
#
# Exercise 8.14 Cars:
#   Write a function that stores information about a car in a dictionary. The 
# function should always receive a manufacturer and a model name. It should 
# then accept an arbitrary number of keyword arguments. Call the function with 
# the required information and two other name-value pairs, such as a color or 
# an optional feature. Your function should work for a call 
# like this one:
#
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
#
#   Print the dictionary that’s returned to make sure all the information was 
# stored correctly.

def make_car(make, model, **car_model):
    """
    Build a dictionary containing information about a car.
    """
    car_model['manufacturer'] = make
    car_model['model'] = model
    return car_model

car_specifications = make_car('lexus', 'is250',
                              color='gray',
                              year=2015,
                              trim='sports')

print(car_specifications)
