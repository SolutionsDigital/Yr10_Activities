# File : Act06_proj2.py 
# Name : Michael Mathews
# Date :  1/4/19
""" Given a list of numbers the program will
print the list and then print the sum
and the product of numbers in the list
"""

# List of Integers for sample data
number_List = [2,3,4,5,6]

# function to add the list numbers
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

# function to multiply the list numbers
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

# welcome the user to the app
print("Welcome to the List Sum and Product app")
# leaves a blankl line in the output
print()

# prints the list
print (number_List)

# leaves a blankl line in the output
print()

# prints the return value of the sum_list function
print("The Sum of Values in the list is" ,sum_list((number_List)))
print()
# prints the return value of the multiply_list function
print("The product of Values in the list is" ,multiply_list((number_List)))
