"""
File : Act03_proj1.py   Name : Michael Mathews  Date : 25/01/2020
Program Purpose :12 rows of the User entered times tables displayed
"""

num=int(input("Suggest an integer for the times tables : "))
print("Here is the times tables for ",num)

for i in range(1,13):
    print(i , "  x  ", num, " = ",i * num)

