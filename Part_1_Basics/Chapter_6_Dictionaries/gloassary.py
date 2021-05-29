# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.3 Glossary:
#   A Python dictionary can be used to model an actual dictionary. However, to 
# avoid confusion, let’s call it a glossary.
# 
# • Think of five programming words you’ve learned about in the previous 
#   chapters. Use these words as the keys in your glossary, and store their 
#   meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print 
#   the word followed by a colon and then its meaning, or print the word on one 
#   line and then print its meaning indented on a second line. Use the newline 
#   character (\n) to insert a blank line between each word-meaning pair in 
#   your output.

glossary = {
    'comment': 'A text or note that the interpreter ignores.',
    'loop': 'Used to iterate over a sequence or iterable objects.',
    'list':'Is a collection of items in a particular order.',
    'syntax':'Are rules that defines how is a program is written and '
    'interpreted.',
    'variable':'Is a named location used to store data.'
    }

key = 'comment'
print(f"{key.title()}: {glossary['comment']}")

key = 'loop'
print(f"{key.title()}: {glossary['loop']}")

key = 'list'
print(f"{key.title()}: {glossary['list']}")

key = 'syntax'
print(f"{key.title()}: {glossary['syntax']}")

key = 'variable'
print(f"{key.title()}: {glossary['variable']}")