# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/30/2021
#
# Chapter 8: Functions
#
# Exercise 8.8 User Albums:
#   Start with your program from Exercise 8-7. Write a while loop that allows 
# users to enter an album’s artist and title. Once you have that information, 
# call make_album() with the user’s input and print the dictionary that’s 
# created. Be sure to include a quit value in the while loop.

def make_album(artist, album, tracks = None):
    """
    Return a dictionary of a music album.
    """
    music_album = {
        'artist': artist,
        'album': album
        }
    if tracks:
        music_album['tracks'] = tracks
    return music_album

input_artist = "\nWho is the artist? "
input_album = "What is the name of the album? "
quit_message = "Enter 'quit' to stop. "

while True:
    artist = input(input_artist)
    if artist == 'quit':
        break

    album = input(input_album)
    if album == 'quit':
        break

    album = make_album(artist, album)
    print(album)