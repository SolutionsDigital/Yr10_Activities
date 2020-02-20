"""
File : Act05_proj1.py 
Name : Michael Mathews
Date : 02/02/2020
Program Purpose :Display List and using the index value
display the first and second last list values
"""

# List sample for output
myList=[1,2,3,4,5,6]
#shows list elements inside the square brackets
print(myList)

#shows list elements in single column
for i in range(6):
    print(myList[i])

print()    # Leaves a blank line

#identify the first list element at index 0   
print("The first element at index 0 is :",myList[0])
 #identify the seciond last list element at index -2 
print("The second last element at index -2 is :",myList[-2])
