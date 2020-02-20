"""
File : Act01_proj4.py  
Name : Michael Mathews  Date :25/01/2020
Program Purpose : The user enters the  
Employee ID, Hourly Rate and Hours Worked.
Weekly wage is calculated and stored as variable
This info will be displayed on the screen in a string
"""

# User Prompted to Enter their EmployeeID
EmpID= input("Enter your EmployeeID Number : ")
# User Prompted to Enter their HourlyRate
HourlyRate = float(input("Enter your Hourly rate : "))
# User Prompted to Enter their HoursWorked
HoursWorked =float(input("Enter your Hours worked :"))
# Calculates Weekly Salary Multplying HoursWorkrd by HourlyRate
# Note use of float (from_string) conversion for decimals 
WeekSalary =HourlyRate * HoursWorked  
# Leaves a Line space between user inputs and print output
print()

# User Feedback with print function for ID and HourlyRate
print ("This pay slip for ID No :" +EmpID + "- Hourly Rate $",HourlyRate)
# User Feedback with print function for HoursWorked and Weekly Salary
# Note use of Float rounding to 2 decimals for WeekSalary using %.2f" %
print ("Total wage for working ",HoursWorked, "this week is $ %.2f" %WeekSalary)
