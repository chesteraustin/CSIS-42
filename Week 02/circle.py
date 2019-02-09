# circle.py
# Chester Austin
# 02/06/2019
# Python 3.7.2
# Description: Program to calculate circumfrance and area of a circle

# Value of PI as constant
PI = 3.1415

# Ask user for radius of Circle
radius = float(input ("Please enter the radius of circle (in inches) ")) # radius

# Calculate area
circle_area = (PI) * (radius **2) 

# Calculate circumfrance
circle_circumfrance = 2 * PI * radius 

print("A circle with radius %.1f inches has" %radius)
print("circumfrance: %.1f inches" %circle_circumfrance)
print("area: %.1f square inches" %circle_area)

'''
Please enter the radius of circle (in inches) 12
A circle with radius 12.0 inches has
circumfrance: 75.4 inches
area: 452.4 square inches
'''