# Python Crash Course: A Hands-On, Project-Based Introduction To Programming
#
# Name: Mark Lester Apuya
# Date: 05/27/2021
#
# Chapter 5: If Statements
#
# Exercise 5.1 Alien Color #2:
#   Choose a color for an alien as you did in Exercise 5-3, and write an if-else 
# chain.
#
# • If the alien’s color is green, print a statement that the player just 
#   earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just
#   earned 10 points.
# • Write one version of this program that runs the if block and another that 
#   runs the else block.

# Runs if block
alien_color = 'green'
print(f"Alien color: {alien_color}")
if alien_color == 'green':                                                
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points.")


# Runs else block
alien_color = 'red'
print(f"\nAlien color: {alien_color}")
if alien_color == 'green':                                                
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points.")