"""  This section is called a doc string
File : Act01_proj1.py 
Name : Michael Mathews
Date :18/08/19
Program Purpose : Having the user enter Four numbers
These numbers will be added then numbers are multiplied
"""

# Prompt user for Four numbers
# int used to change these entries into integers
print("Please enter 3 Numbers as prompted by program")
Numb1= int(input("Enter the first Number : "))
Numb2= int(input("Enter the second Number : "))
Numb3= int(input("Enter the third Number : "))
Numb4= int(input("Enter the fourth Number : "))

# calculations for addition and multiplication
AddNumbers= Numb1 + Numb2 + Numb3 + Numb4
MultiplyNumbers= Numb1 * Numb2 * Numb3 * Numb4
print()   # Leaves one line blank

# feedback of calculation results and Farwell
print(" The Numbers added = " , AddNumbers)
print(" The Numbers Multiplied = " , MultiplyNumbers)
print(" Thankyou :o) " )

