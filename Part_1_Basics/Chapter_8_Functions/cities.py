# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 8: Functions
#
# Exercise 8.5 Cities:
#   Write a function called describe_city() that accepts the name of a city and 
# its country. The function should print a simple sentence, such as Reykjavik 
# is in Iceland. Give the parameter for the country a default value. Call your 
# function for three different cities, at least one of which is not in the 
# default country.

def describe_city(city, country = 'unied states'):
    """
    Describes a city.
    """
    print(f"{city.title()} is in {country.title()}.")

describe_city('honolulu')
describe_city('los angeles')
describe_city('tokyo', 'japan')