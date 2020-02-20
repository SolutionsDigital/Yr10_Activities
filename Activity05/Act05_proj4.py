"""
File : Act05_proj4.py 
Name : Michael Mathews     Date : 02/02/2020
Program Purpose: : Investigate common factors
for user defined integers and upper limit
"""

# upper boundary defined by user
upper = int(input("what is the upper boundary :"))
# create list = l ready for data
list=[]

# prompt user for fist factor
m = int(input("what is the first factor :"))
# prompt user for second factor
n = int(input("what is the second factor :"))

# loop through numbers 1 to upper
for i in range(1,upper):
    if (i%m==0) and (i%n==0): #check divisibility
        list.append(str(i)) # add if divisibility by both

print(', '.join(list)) # print list items


