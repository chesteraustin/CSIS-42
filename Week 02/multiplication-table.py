# multiplication-table.py
# Chester Austin
# 02/06/2019
# Python 3.7.2
# Description: Program to display multiplication table of float values 0.1, 0.2 and 0.3

# Header of table
print("       0.1    0.2    0.3")
# Row 0.1
row1 = 0.1
print("%.1f    %.2f   %.2f   %.2f" %(row1, row1*0.1, row1*0.2, row1*0.3))

# Row 0.2
row2 = 0.2
print("%.1f    %.2f   %.2f   %.2f" %(row2, row2*0.1, row2*0.2, row2*0.3))

# Row 0.3
row3 = 0.3
print("%.1f    %.2f   %.2f   %.2f" %(row3, row3*0.1, row3*0.2, row3*0.3))

'''
       0.1    0.2    0.3
0.1    0.01   0.02   0.03
0.2    0.02   0.04   0.06
0.3    0.03   0.06   0.09
'''