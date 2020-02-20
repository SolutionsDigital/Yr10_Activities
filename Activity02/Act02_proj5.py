"""
File : Act02_proj5.py   Name : Michael Mathews   Date : 25/01/2020
Program Purpose : roll two die (x100) keeping track of total die value occurances
for die total values of  2 (1+1)  .. 3 (2+1),(1+2) ......   12(6+6)
output the totals for each total die value and occurance
"""
# allows use of random value for die roll
import random
dieTotal2=0
dieTotal3=0
dieTotal4=0
dieTotal5=0
dieTotal6=0
dieTotal7=0
dieTotal8=0
dieTotal9=0
dieTotal10=0
dieTotal11=0
dieTotal12=0
print("Welcome to the double dice roll simulation")
for i in range(1000):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    diceValue=die1 +die2
    if diceValue==2:
        dieTotal2=dieTotal2+1
    elif diceValue==3:
        dieTotal3=dieTotal3+1
    elif diceValue==4:
        dieTotal4=dieTotal4+1
    elif diceValue==5:
        dieTotal5=dieTotal5+1
    elif diceValue==6:
        dieTotal6=dieTotal6+1
    elif diceValue==7:
        dieTotal7=dieTotal7+1
    elif diceValue==8:
        dieTotal8=dieTotal8+1
    elif diceValue==9:
        dieTotal9=dieTotal9+1
    elif diceValue==10:
        dieTotal10=dieTotal10+1
    elif diceValue==11:
        dieTotal11=dieTotal11+1
    else: 
        dieTotal12=dieTotal12+1
print("Total of Two occurrence was :",dieTotal2)
print("Total of Three occurrence was :",dieTotal3)
print("Total of Four occurrence was :",dieTotal4)
print("Total of Five occurrence was :",dieTotal5)
print("Total of Six occurrence was :",dieTotal6)
print("Total of Seven occurrence was :",dieTotal7)
print("Total of Eight occurrence was :",dieTotal8)
print("Total of nine occurrence was :",dieTotal9)
print("Total of Ten occurrence was :",dieTotal10)
print("Total of Eleven occurrence was :",dieTotal11)
print("Total of Twelve occurrence was :",dieTotal12)
