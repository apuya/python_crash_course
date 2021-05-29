# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.9 Favorite Places:
#   Make a dictionary called favorite_places. Think of three names to use as 
# keys in the dictionary, and store one to three favorite places for each 
# person. To make this exercise a bit more interesting, ask some friends to 
# name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

favorite_places = {
   'mark': ['hawaii', 'oregon coast', 'california'],
   'troy': ['laguna beach', 'disney land', 'santa monica'],
   'jaxon': ['lanikai beach', 'joshua tree', 'yosemite']
   }

for name, places in favorite_places.items():
   print(f"\n{name.title()}'s favorite places:")
   for place in places:
      print(place.title())