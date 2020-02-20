"""
File : Act04_proj2.py 
Name : Michael Mathews    Date : 25/01/2020
Program Purpose : Calculate and display the Area of a Rectangle
When given the base and height by user input
"""
# Area calculation function
def RectArea(b,h):
    area = b*h
    print()
    print("Area of the Rectangle is : %.2f" %area)
    
# perimeter calculation function
def RectPerimeter(b,h):
    perimeter = 2*b+2*h
    print()
    print("Perimeter of the Rectangle is : %.2f" %perimeter)
    
# enter base and height values ready for passing to the functions
base = float(input('Enter the Base of the Rectangle :'))
height = float(input('Enter the Height of the Rectangle :'))

# calls the Area function with two input parameters of base and height
RectArea(base,height)
# calls the Perimter function with two input parameters of base and height
RectPerimeter(base,height)
