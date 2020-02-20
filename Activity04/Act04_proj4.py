"""
File : Act04_proj4.py 
Name : Michael Mathews   Date : 25/01/2020
Program Purpose : Area of Triangle Rectangle and square
"""

# user defined function for area of Triangle
def AreaTriangle(b,h):
    triArea=0.5*b*h
    print("The Triangle area is ",triArea," square units")

# user defined function for area of Rectangle
def AreaRectangle(b,h):
    rectArea=b*h
    print("The Rectangle area is ",rectArea," square units")

# user defined function for area of Square
def AreaSquare(b):
    squArea=b*b
    print("The square area is ",squArea," square units")

# prompt User for Measurements 
base=int(input("What is the base of the shape : "))
height=int(input("What is the height of the shape : "))

# Out put Function Calculations
print()
AreaTriangle(base,height)
print()
AreaRectangle(base,height)
print()
AreaSquare(base)

