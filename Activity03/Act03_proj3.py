"""
File : Act03_proj3.py 
Name : Michael Mathews    Date : 25/01/2020
# Program Purpose : printing Prime Number status up to 20
"""
for n in range(1, 20):
     for x in range(2, n):
          if n % x == 0:
               print(n, 'equals', x, '*', n//x)
               break
     else:
         # loop fell through without finding a factor
         print( n,' - is a prime number')

