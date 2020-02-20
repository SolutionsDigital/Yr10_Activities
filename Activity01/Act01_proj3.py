"""
File : Act01_proj3.py  
Name : Michael Mathews
Date :25/01/2020
Program Purpose: The user enters the Name, Address and Age
This info will be displayed on the screen including age next year.
"""

# request for user to enter their first name
FName= input("Enter your first name : ")
# request for user to enter their Surname
Surname= input("Enter your surname : ")
# request for user to enter their Suburb
Suburb = input("Enter your suburb :")
# request for user to enter their age
# note use of int to change user entry to integer
Age = int(input("Enter your age :"))

# print function used to output message to screen
print (FName+" " + Surname + " from " + Suburb +" will be ", Age+1, "next year")

