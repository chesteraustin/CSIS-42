# printCS_withLetter.py
# Chester Austin
# 01/30/2019
# Python 3.7.2
# Description: Write a program that asks for a character INPUT from the keyboard and then OUTPUTS a large block letter "C" 
# composed of that character. For example, if the user inputs the character "X", then the output should look as follows:

x = input("Enter a letter ")

print ("************************************************************")
print ("") #Blank line 1
print ("") #Blank line 2
print ("                 %s %s %s                      S S S           " %(x,x,x))
print ("               %s       %s                   S     S          " %(x,x))
print ("              %s                            S                 " %(x))
print ("             %s                              S                " %(x))
print ("             %s                               S S S           " %(x))
print ("             %s                                     S         " %(x))
print ("              %s                                    S         " %(x))
print ("               %s      %s                    S     S          " %(x,x))
print ("                %s %s %s                       S S S           " %(x,x,x))
print ("") #Blank line 1
print ("") #Blank line 2
print ("************************************************************")
print ("")
print ("        Computer Sciencse is Cool Stuff!!!")

'''
Enter a letter P
************************************************************


                 P P P                      S S S
               P       P                   S     S
              P                            S
             P                              S
             P                               S S S
             P                                     S
              P                                    S
               P      P                    S     S
                P P P                       S S S


************************************************************

        Computer Sciencse is Cool Stuff!!!
'''