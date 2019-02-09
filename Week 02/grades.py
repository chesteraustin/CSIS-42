# grades.py
# Chester Austin
# 02/06/2019
# Python 3.7.2
# Description: Program to calculate grades based on score

# User input of score
userScore = float(input ("Please enter grade percentage ")) # score

# Validate entry
if userScore < 0 or userScore > 100 : # check to see if user score is between 0 and 100
    print("Invalid percent score.  Please enter a value between 0 and 100")
    userScore = float(input ("Please enter grade percentage ")) # score

# Display grade
if userScore >= 90 : # Grade of A
    print("The letter grade is an 'A'")
elif userScore >= 80 and userScore < 90: # Grade of B
    print("The letter grade is a 'B'")
elif userScore >= 70 and userScore < 80: # Grade of C
    print("The letter grade is a 'C'")
elif userScore >= 60 and userScore < 70: # Grade of D
    print("The letter grade is a 'D'")
else : # default of F
    print("The letter grade is an 'F")

'''
Please enter grade percentage -1
Invalid percent score.  Please enter a value between 0 and 100
Please enter grade percentage 75
The letter grade is a 'C'
'''