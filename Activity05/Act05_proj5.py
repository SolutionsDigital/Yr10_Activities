"""
File : Act05_proj5.py 
Name : Michael Mathews    Date : 1/4/19
Program Purpose : Add Multiples of a number to a list
then print the list of Multiples up to a max of 100

factorlist =[] of sample numbers for output if divisible by n  
using if i%n==0 (ie div n with 0 left over)= Multiple of n
show all factors up to 100 in a row structure
then outputs the first 4 multiples and last 4 multiples
"""

# Prompt user for integer
n=int(input("What numer would you like to see Multiples : "))

factorlist=[]   # set container for list of factors

for i in range(1,100):   # iterate through numbers from 1 to 99
    if i%n==0:            # check to see if n is a Multiple
        factorlist.append(str(i))   # if it is a Multiple append to list

print(', '.join(factorlist))    # print list
print(factorlist[0:4])          # print first 4
print(factorlist[-5:-1])        # print last 4
 
