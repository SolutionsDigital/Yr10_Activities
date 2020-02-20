"""
Volume solver - Collection of methods for calculating various volume formulas
using floats or decimals yet
"""
import math

def volume_of_cube():
    side =float( input("side ? "))
    answer = side * side * side
    print(f"Volume_of_cube with side {side} is {answer} cubic units")

def volume_of_box():
    width = float(input("Width ? "))
    length = float(input("Length ? "))
    depth = float(input("Depth ? "))
    vol = width * length * depth
    print("Volume of rectangle with ")
    print(f"width = {width}, length = {length}, depth = {depth}")
    print(f"   is   {vol} cubic units")

    
def volume_of_sphere():
    radius = float(input("Radius? "))
    answer = (4/3) * (math.pi * radius**3)
    print(f"Volume of sphere with radius {radius} is {answer}")

# main function -  entry point for the program
# prints a simple menu - you make the choice and supply the values

def main():
    running = True
    while (running):
        # print the menu
        print()  # blank line
        print("Welcome to the Volume Solver!")
        print("-------------------------------")
        print("1) Volume of a cube")
        print("2) Volume of a box")
        print("3) Volume of a sphere")
        print("X) Exit")
        print()  # blank line

        # process the user input
        choice = input(" Your choice ? ")
        if choice == "1":
            volume_of_cube()

        elif choice == "2":
            volume_of_box()
            
        elif choice == "3":
            volume_of_sphere()
        else:
            print("Goodbye!")
            break

# If we're running this module as the main program, execute main()
if __name__ == "__main__":
    main()
