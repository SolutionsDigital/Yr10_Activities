"""
File : Act04_proj3.py 
Name : Michael Mathews     Date : 25/01/2020
Program Purpose : Calculate and display the Area and Circumference
of a circle  When given the radius by user input
"""
import math
    
# function to calculate the area and circumference
def CircleSize(r):

    area = math.pi * r * r
    circumference = math.pi * 2 * r
    print()
    print("Area of the circle is : %.2f" %area)
    print()
    print("Circumference of the circle is : %.2f" %circumference)


radius = float(input('Enter the radius of the circle :'))
CircleSize(radius)

            
