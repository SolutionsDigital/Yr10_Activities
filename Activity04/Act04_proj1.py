"""
File : Act04_proj1.py 
Name : Michael Mathews   Date : 02/02/2020
Program Purpose :Sing Happy Birthday using functions
for the repeated lines
"""


def HappyBday():
    print("Happy Birhday to you ")


def Welcome(name):
    HappyBday()
    HappyBday()
    print("Happy Birthday dear", name)
    HappyBday()


print("so it is your birthday")
User = input("What is your Name :")
Welcome(User)
