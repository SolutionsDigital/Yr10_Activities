"""
File : Act03_proj4.py    Name : Michael Mathews    Date : 25/01/2020
Python program to prompt the use to enter numbers for data
Then after using 0 to finish oupt the Sum and Average
"""
# User Information
print("Input some integers to calculate their sum and average")
print("Press Enter after each input value and 0 to Finish.")
print()
# Prompt User for numbers
print("Input some numbers")
count = 0
sum = 0.0
number = 1
while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1
if count == 0:
   print("Input some numbers")
else:
   print("Sum of the entered numbers =  ", sum)
   print("Average of the entered numbers = ", sum /(count-1))
	
