# input.py
# Chester Austin
# 01/30/2019
# Python 3.7.2
# Description: Program to take input in Python

name = input ("Please enter Your Name: ") # this is a string
weightLbs = float(input ("Please enter Your weight in lbs: ")) # a float
age = int (input ("Please enter your age (whole number): ")) # an integer
weightKg = weightLbs * 0.453952
title = "Human"

print ("Hello ", title,name, "your weight is")
print (weightLbs, "lbs")
print("which equals = %.2f" %weightKg, end=' ') #end=' ' prevents new line
print ("kilograms ")

'''
Please enter Your Name: Chester
Please enter Your weight in lbs: 150
Please enter your age (whole number): 35
Hello  Human Chester your weight is
150.0 lbs
which equals = 68.09 kilograms
'''