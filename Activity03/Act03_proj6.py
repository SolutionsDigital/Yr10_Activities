"""
File : Act03_proj6.py   Name : Michael Mathews  Date : 25/01/2020
Python Program to find the factors of a number
 using a defined function for the 
"""

def print_factors(x):
   # This function takes a number and prints the factors
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# uncomment the following line to take input from the user
num = int(input("Enter a number: "))
print_factors(num)

