"""  File : Act02_Proj3.py   # Name : Michael Mathews   Date : 25/01/2020
Program Purpose : Rolling 2 Die and keeping track of
Roll number and Total and a Win with(7 or 11) or loose message
"""

# allows the use of Random Numbers
import random

# sets Rollnumber and RollAgain to defaults
RollNumber = 0
RollAgain = 'y'

# sets up loop until "x" is selected
while RollAgain != 'x':
    # rolls die1 and die2 num 1...6
    die1 = int(random.randint(1, 6))
    die2 = int(random.randint(1, 6))
    # Output to screen the two values
    print("The total on Die 1 is :", die1)
    print("The total on Die 2 is :", die2)
    print()
    # add the values for the two die
    TotalDie = die1 + die2
    # add 1 to roll number
    RollNumber = RollNumber + 1

    # prints total and rollnumber to screen
    print("Roll number : ", RollNumber, "had total value of :", TotalDie)
    print()
    if TotalDie in (7, 11):
        print("rolling a ", TotalDie, "makes you a winner")
        print()
    else:
        print("Sorry You loose")
        print()
    RollAgain = input("Roll again or Press x ")

# farewell user
print('Bye Bye')
