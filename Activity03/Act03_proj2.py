"""
File : Act03_Py_p2.py
Name : Michael Mathews     Date : 25/01/2020
Program Purpose : Loan Repayments Calculator
Calculate weekly and monthly payment keep track monthly payments
"""
# Welcome the user
print("Welcome to the Loan Calculator")
# Allow 1 line space in Output
print()

# Prompt User for Loan amount
Loan_Amount = int(input("Enter the amount to be borrowed $ "))
# Allow 1 line space in Output
print()

# Calculations for weekly and monthly payments
weeklyPayment = Loan_Amount / 52
monthlyPayment = Loan_Amount / 12

# display to user weekly and monthly payments using print
print("Weekly payment $", round(weeklyPayment, 2))
print("Monthly payment $", round(monthlyPayment, 2))
# Allow 1 line space in Output
print()

# sets month counter to 0
month = 0

# loops through months showing the payment off the loanAmount
while Loan_Amount > 0:
    month = month+1
    print("$ %15.3f" % Loan_Amount, " - Month ", month,)
    Loan_Amount = Loan_Amount - monthlyPayment
