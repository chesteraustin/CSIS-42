# rock-paper-scissors.py
# Chester Austin
# 02/06/2019
# Python 3.7.2
# Description: Program to play rock, paper, scissors

# import random library
import random

# User input of score
player1 = input ("Choose a throw: (R)ock, (P)aper, or (S)cissors ") # player 1 input
player2 = random.randint(1,3)

# Convert choices to numeric values for comparison
if player1 is 'r' or player1 is 'R':
    player1_value = 1
    player1_text = "Rock"
elif player1 is 'p' or player1 is 'P':
    player1_value = 2
    player1_text = "Paper"
elif player1 is 's' or player1 is 'S':
    player1_value = 3
    player1_text = "Scissors"

if player2 is 1:
    player2_value = 1
    player2_text = "Rock"
elif player2 is 2:
    player2_value = 2
    player2_text = "Paper"
elif player2 is 3:
    player2_value = 3
    player2_text = "Scissors"

print("Player1 chose %s" %player1_text)
print("Player2 chose %s" %player2_text)
# compare choices
# rock vs paper (1 v 2) - Lose
# rock vs scissors  (1 v 3) - Win
# paper vs rock (2 v 1) - Win
# paper vs scissors  (2 v 3) - Lose
# scissors vs rock (3 v 1) - Lose
# scissors vs paper (3 v 2) - Win

if player1_value is player2_value:
    print("There is a tie.  Both players chose %s" %player1_text)

# player1 chose rock
if player1_text is 'Rock':
    if player2_value is 2:
        print("Player 1 loses.")
    elif player2_value is 3:
        print("Player 1 wins.")

# player1 chose paper
elif player1_text is 'Paper':
    if player2_value is 1:
        print("Player 1 wins.")
    elif player2_value is 3:
        print("Player 1 loses.")

# player1 chose scissors
elif player1_text is 'Scissors':
    if player2_value is 1:
        print("Player 1 loses.")
    elif player2_value is 2:
        print("Player 1 wins.")

'''
Game 1
Choose a throw: (R)ock, (P)aper, or (S)cissors r
Player1 chose Rock
Player2 chose Rock
There is a tie.  Both players chose Rock

Game 2
Choose a throw: (R)ock, (P)aper, or (S)cissors p
Player1 chose Paper
Player2 chose Rock
Player 1 wins.

Game 3
Choose a throw: (R)ock, (P)aper, or (S)cissors s
Player1 chose Scissors
Player2 chose Scissors
There is a tie.  Both players chose Scissors

Game 4
Choose a throw: (R)ock, (P)aper, or (S)cissors s
Player1 chose Scissors
Player2 chose Paper
Player 1 wins.
'''