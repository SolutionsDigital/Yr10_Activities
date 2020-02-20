""" File : Act02_Py_p2.py 
   Name : Michael Mathews    Date : 25/01/2020
   Program Purpose : Prompt user for 4 marks then
   # Calculate Grade using the average mark (of the 4 marks)
   # where A >= 90; B>=80;C >= 60; D>=50; E<50
   # output Average and Overall Grade
   """
# welcome the User
print("welcome to the Average Mark Grade calculator")
# Creates a 1 line space between content
print()
# prompts the user to enter 4 marks
Mark1 = int(input("Enter Test Result 1 :"))
Mark2 = int(input("Enter Test Result 2 :"))
Mark3 = int(input("Enter Test Result 3 :"))
Mark4 = int(input("Enter Test Result 4 :"))
print()
# calculates the average mark
AverageMark = (Mark1+Mark2+Mark3+Mark4)/4
# shows the average mark on the screen
print('Your Average is ', AverageMark)
# selection of grade on AverageMark
# with user feedback showing grade
if AverageMark >= 95:
    print('Your Grade is A+')
elif AverageMark >= 90:
    print('Your Grade is A')
elif AverageMark >= 80:
    print('Your Grade is B')
elif AverageMark >= 60:
    print('Your Grade is C')
elif AverageMark >= 50:
    print('Your Grade is D')
else:
    print('Your Grade is E')
