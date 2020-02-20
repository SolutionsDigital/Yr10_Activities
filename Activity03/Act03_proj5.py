"""
File : Act03_proj5.py    Name : Michael Mathews   Date : 25/01/2020
Program Purpose : printing square and cubic numbers
Up to a user defined Ceiling Number.
"""
# Prompt User for Ceiling
Ceiling =int(input("What is the Ceiling for numbers :"))
# Feedback for User
print("Here are the Square and Cubic numbers up to ",Ceiling)
# blank line spacer
print()
# adjusting Ceiling to add 1
Ceiling = Ceiling +1
# Setting up Headings
print('{:>7}'.format("square"),'{:>7}'.format("cube"))
# printing square and cube values into format - '{:10d}'.format()
for i in range (1,Ceiling):
    square = i*i
    cube = i**3
    print('{:7d}'.format(square),'{:7d}'.format(cube))

