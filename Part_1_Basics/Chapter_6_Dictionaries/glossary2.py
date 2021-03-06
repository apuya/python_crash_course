# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/28/2021
#
# Chapter 6: Dictionaries
#
# Exercise 6.4 Glossary 2:
#   Now that you know how to loop through a dictionary, clean up the code from 
# Exercise 6-3 (page 99) by replacing your series of print() calls with a loop 
# that runs through the dictionary’s keys and values. When you’re sure that 
# your loop works, add five more Python terms to your glossary. When you run 
# your program again, these new words and meanings should automatically be 
# included in the output.

glossary = {
    'comment': 'A text or note that the interpreter ignores.',
    'loop': 'Used to iterate over a sequence or iterable objects.',
    'list':'Is a collection of items in a particular order.',
    'syntax':'Are rules that defines how is a program is written and '
    'interpreted.',
    'variable':'Is a named location used to store data.'
    }

for key, value in glossary.items():
    print(f"\n{key.title()}: {value}")