"""
File : Act02_Py_p1.py 
Name : Michael Mathews    Date : 25/01/2020
This program will accept the score from the user and find the Average
The average is used in a selection Construct to
check on PASS or Fail  - Pass reuires  >= 65
"""

# Welcomes the user
print("Welcome to the Pass Fail Calculator")
# Puts a line break in after the welcome
print()

# makes the program loop until x is entered
while quit !='x':
    # three marks entered as converted to float (from input default string)
    mark1= float(input('Please enter your first mark out of 100 -  mark1:'))
    mark2= float(input('Please enter your Second mark out of 100 -  mark2:'))
    mark3= float(input('Please enter your Third mark out of 100 -  mark3:'))
    # Average mark calculated with equation
    AvMark = (mark1+mark2+mark3)/3
    print("Your Average mark is ", round(AvMark,1))
# checks if average is above or equal to 65
    if AvMark >=65:
        print ('well done you passed')  # Congratulations message printed
    else:
        print ('bugger you failed this time')# bugger message printed
    print()
    # Puts a line break in before Option to quit with quit offering 
    quit = input('Press ''x'' to quit or Any key to try again ')

# Farewell to the uer
print(" Thanks for using the Pass Fail Calculator")    
