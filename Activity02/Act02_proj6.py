"""
Code for top of your  Activity02_Q6.py 
Name : Michael Mathews    Date :25/1/2020
Program Purpose : The computer will simulate a three dice roll.
Winners declared on any Triple or Double otherwise unlucky try again
"""

import random
# rolling thtee dice
die1 = int(random.randint(1,6))
die2 = int(random.randint(1,6))
die3 = int(random.randint(1,6))
# output the die values
print("The value on Die 1 is :", die1)
print("The value on Die 2 is :", die2)
print("The value on Die 3 is :", die3)
# calculate the three die Totals
TotalDie = die1 + die2 + die3
print()
# output the three die Totals
print("The  Total  value  is :", TotalDie)
print()
# checking for triples
if die1==die2 and die2 == die3:
    print("Big Winner !  You got a Triple")
# checking for doubles    
elif die1==die2 or die2 == die3 or die3 == die1:
    print("Winner !  You got a double")
# giving the loser feedback
else :
    print("Unlucky Try Again")

