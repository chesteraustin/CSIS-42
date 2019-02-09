# voting.py
# Chester Austin
# 02/09/2019
# Python 3.7.2
# Description: Program to determine if user can vote
'''
Directions:
Write a program to determine if the user can vote. The program will ask the user a series of questions - age, citizenship and registration. The user will receive a message as to whether or not s/he may vote -- yes, no (with a reason - too young, not a citizen, hasn't registered to vote).

Be sure to test your program at least 4 times:

The user can vote
The user can't vote because they are not old enough.
The user can't vote because they are not old enough and not a citizen.
The user can't vote because they are not old enough, not a citizen, not registered.
Note: You must be over 18, registered , and a citizen to vote.
'''
# User input of height in feet and inches
print("Hello.  Please enter your height ")
userHeightFt = float(input ("Feet: ")) # feet
userHeightIn = float(input ("Inches: ")) # inches

# Calculate in inches
total_heightIn = (userHeightFt * 12) + userHeightIn

# Display message
if total_heightIn > 72 : # height is above 72
    print("You are above average height.")
elif total_heightIn >= 60 and total_heightIn <= 72: # height is between 60 and 72
    print("You are average height.")
elif total_heightIn <= 60 : # height is below 60
    print("You are below average height.")

'''
Hello.  Please enter your height
Feet: 5
Inches: 8
You are average height.
'''