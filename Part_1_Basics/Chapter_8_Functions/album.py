# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/29/2021
#
# Chapter 8: Functions
#
# Exercise 8.7 Album:
#   Write a function called make_album() that builds a dictionary describing a 
# music album. The function should take in an artist name and an album title, 
# and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album 
# information correctly.
#   Use None to add an optional parameter to make_album() that allows you to 
# store the number of songs on an album. If the calling line includes a value 
# for the number of songs, add that value to the album’s dictionary. Make at 
# least one new function call that includes the number of songs on an album.

def make_album(artist, album):
    """
    Return a disctionary of a music album.
    """
    music_album = {
        'artist': artist,
        'album': album
        }
    return music_album

album = make_album('Pink Sweat$', "At My Worst")
print(album)

album = make_album('Kane Brown', "Worship You")
print(album)

album = make_album('Meduza', "Paradise")
print(album)

# adds optional patameter num_track for the number of tracks in album.

def make_album2(artist, album, num_track = None):
    """
    Return a dictionary of a music album.
    """
    music_album2 = {
        'artist': artist,
        'album': album
        }
    if num_track:
        music_album2['num_track'] = num_track
    return music_album2

album = make_album2('Pink Sweat$', "At My Worst")
print(album)

album = make_album2('Kane Brown', "Worship You")
print(album)

album = make_album2('Meduza', "Paradise", num_track = 6)
print(album)