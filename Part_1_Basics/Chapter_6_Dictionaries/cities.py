# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.11 Cities:
#   Make a dictionary called cities. Use the names of three cities as keys in 
# your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one 
# fact about that city. The keys for each city’s dictionary should be something
# like country, population, and fact. Print the name of each city and all of 
# the information you have stored about it.

cities = {
    'los angeles': {
        'country': 'united states',
        'population': 3967000,
        'fact': 'disney land'
        },
    'honolulu': {
        'country': 'united states',
        'population': 348985,
        'fact': 'waikiki beach'
        },
    'paris': {
        'country': 'france',
        'population': 2161000,
        'fact': 'eiffel tower'
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"The population of the city is {str(population)}.")
    print(f"{city.title()} is the home of {fact}.")