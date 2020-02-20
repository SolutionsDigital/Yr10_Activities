"""
File : Act02_proj4.py
Name : Michael Mathews  Date : 25/01/2020
Program Purpose : roll a die 100 times
keep track of die value occurances
output the totals for each die value
"""

# allows use of random value for die roll
import random

# set the count for each potential dievalue = 0
dieValue1=0
dieValue2=0
dieValue3=0
dieValue4=0
dieValue5=0
dieValue6=0
# welcome user
print("Welcome to the die roll simulation")
# roll die 100 times
for i in range(100):
    die = random.randint(1,6)
    if die==1:
        dieValue1=dieValue1+1
    elif die==2:
        dieValue2=dieValue2+1
    elif die==3:
        dieValue3=dieValue3+1
    elif die==4:
        dieValue4=dieValue4+1
    elif die==5:
        dieValue5=dieValue5+1
    else: 
        dieValue6=dieValue6+1
# print function to output die totals to screen               
print("total of rolls for 1 :",dieValue1)
print("total of rolls for 2 :",dieValue2)
print("total of rolls for 3 :",dieValue3)
print("total of rolls for 4 :",dieValue4)
print("total of rolls for 5 :",dieValue5)
print("total of rolls for 6 :",dieValue6)

