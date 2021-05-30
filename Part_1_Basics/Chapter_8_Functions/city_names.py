# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 8: Functions
#
# Exercise 8.6 City Names:
#   Write a function called city_country() that takes in the name of a city and 
# its country. The function should return a string formatted like this:
#
# "Santiago, Chile"
#
#   Call your function with at least three city-country pairs, and print the 
# values that are returned.

def city_country(city, country):
    """
    returns string: "city, country"
    """
    return(f"{city.title()}, {country.title()}.")

city = city_country('santiago', 'chili')
print(city)

city = city_country('los angeles', 'united states')
print(city)

city = city_country('seattle', 'united states')
print(city)