# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/30/2021
#
# Chapter 8: Functions
#
# Exercise 8.13 User Profile:
#   Start with a copy of user_profile.py from page 149. Build a profile of 
# yourself by calling build_profile(), using your first and last names and 
# three other keyvalue pairs that describe you.

def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
    'mark', 'apuya',
    age=25,
    location='los angeles',
    field='engineering',
    )

print(user_profile)