#############################################################################                                                                      
#                                                                      
#  ,d                                                                   
#  88                                                                   
#MM88MMM  ,adPPYYba,  8b,dPPYba,   8b,dPPYba,    ,adPPYba,  8b,dPPYba,  
#  88     ""     `Y8  88P'   `"8a  88P'   `"8a  a8P_____88  88P'   "Y8  
#  88     ,adPPPPP88  88       88  88       88  8PP"""""""  88          
#  88,    88,    ,88  88       88  88       88  "8b,   ,aa  88          
#  "Y888  `"8bbdP"Y8  88       88  88       88   `"Ybbd8"'  88          
#
#
###############################################################################
import random

# User will input a number representing their score
user = int(input("Enter a number that represents your grade? "))

# Rivals score is automatically generated using the random module
rivals_score = random.randint(1, 100)

# A function that determines the grade and returns what they received
def grade(x):
    if x >= 0 and x < 59:
        return 'F'
    elif x > 59 and x < 60:
        return 'D'
    elif x > 60 and x < 70:
        return 'C'
    elif x > 70 and x < 80:
        return 'B'
    else:
        return 'A'


s = grade(user)

rival = grade(rivals_score)

# Using an if statement to determine who recieved the better score
if rival > s:
    print(" I beat you")
else:
    print("s is the winner")