
# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date:
#
# Chapter 14: Scoring
#
# Exercise 14.6 Refactoring:
# Look for methods that are doing more than one task, and refactor them to organize your code and make it efficient. For example, move 
# some of the code in _check_bullet_alien_collisions(), which starts a new level when the fleet of aliens has been destroyed, to a 
# function called start_new _level(). Also, move the four separate method calls in the __init__() method in Scoreboard to a method 
# called prep_images() to shorten __init__(). The prep_images() method could also help simplify _check_play_button() or start _game() 
# if you’ve already refactored _check_play_button().
#
# NOTE: Before attempting to refactor the project, see Appendix D to learn how to restore the project to a working state if you 
#       introduce bugs while refactoring.