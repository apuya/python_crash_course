# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/21/2021
#
# Chapter 3: Introducing Lists
#
# Exercise 3.8 Seeing the Worl:
# Think of at least five places in the world you’d like to visit.
#
# • Store the locations in a list. Make sure the list is not in alphabetical 
#   order.
# • Print your list in its original order. Don’t worry about printing the list
#   neatly, just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
#   actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without 
#   changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that
#   its order has changed.
# • Use reverse() to change the order of your list again. Print the list to 
#   show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print
#   the list to show that its order 
#   has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical 
#   order. Print the list to show that its order has changed.

locations = [
    'Bali', 'Japan', 
    'Philippines', 'Iceland',
    ]
print(locations)

# sorted(): allows you display the list in alphabetical order without modifying
# the original list
print(sorted(locations))
print(locations)

# reverse = True will sort the list in reverse
print(sorted(locations, reverse = True))
print(locations)

# reverse() will reverse the order of the list
locations.reverse()
print(locations)

locations.reverse()
print(locations)

# sort() will change the order of the list alphabeticaly and reverse alphabettical
locations.sort()
print(locations)

locations.sort(reverse = True)
print(locations)