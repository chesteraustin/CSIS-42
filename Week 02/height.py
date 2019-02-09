# height.py
# Chester Austin
# 02/06/2019
# Python 3.7.2
# Description: Program to Compute Height given by user

# User input of height in feet and inches
print("Hello.  Please enter your height ")
userHeightFt = float(input ("Feet: ")) # feet
userHeightIn = float(input ("Inches: ")) # inches

# Calculate in inches
total_heightIn = (userHeightFt * 12) + userHeightIn

# Display conversion
print ("Your height of %.0f feet and %.0F inche(s) is %.0f inches." %(userHeightFt, userHeightIn, total_heightIn))

'''
Hello.  Please enter your height
Feet: 5
Inches: 8
Your height of 5 feet and 8 inche(s) is 68 inches.
'''