# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.5 Rivers:
#   Make a dictionary containing three major rivers and the country each river 
# runs through. One key-value pair might be 'nile': 'egypt'.
#
# • Use a loop to print a sentence about each river, such as The Nile runs 
#   through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

major_rivers = {'amazon': 'brazil',
                'nile': 'egypt',
                'mississippi': 'united states'}

for river, country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
for river in major_rivers.keys():
    print(river.title())

print("\nCountry included in the dictionary:")
for country in major_rivers.values():
    print(country.title())