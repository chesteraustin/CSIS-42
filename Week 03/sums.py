# sums.py
# Chester Austin
# 02/09/2019
# Python 3.7.2
# Description: Program to determine the sums of 4 numbers
'''
Write a program that asks the user to enter 4 numbers (positive or negative).
The program shows:
the sum of all numbers (sumAll)
the sum of positive numbers (sumPos),
the sum of negative numbers (sumNeg)
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