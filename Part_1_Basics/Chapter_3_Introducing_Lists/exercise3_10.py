# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/22/2021
#
# Chapter 3: Introducing Lists
#
# Exercise 3.10 Every Function:
# Think of something you could store in a list. For example, you could make a 
# list of mountains, rivers, countries, cities, languages, or anything else 
# you’d like. Write a program that creates a list containing these items and 
# then uses each function introduced in this chapter at least once.

languages = ['c++', 'python', 'c', 'java']
print(f"Languages: {languages}")

# append() add new element at the end of the list
languages.append('html')
print(f"Using append() function: {languages}")

# insert() add new element at any position in the list\
languages.insert(2, 'c#')
print(f"Using insert() function: {languages}")

# del() deletes an item from the list
del languages[3]
print(f"Using del() function: {languages}")

# pop() allows you to use the value of the item you remove from the list
popped_item = languages.pop(4)
print(f"Item removed using the pop() function: {popped_item}")
print(f"Using pop() function: {languages}")

# remove() allows you to remove a value from the list
languages.remove('c#')
print(f"Using remove() function: {languages}")

# sort() sort the the list alphabetically
languages.sort()
print(f"Using sort() function: {languages}")

languages = ['c++', 'python', 'java']

# sorted() function allows you to display the list alphabetically without 
# modifying the original list
print(f"List using the sorted() function: {languages}")
print(f"List without the sorted() function: {languages}")

# reverse() reverses the order of the list
languages.reverse()
print(f"Using the reverse() function: {languages}")

# len() finds the length of the list
print(f"Using len() to find the length of the list: {len(languages)}")