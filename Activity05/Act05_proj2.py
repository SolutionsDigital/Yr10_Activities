"""
File : Act05_proj2.py 
Name : Michael Mathews    Date : 02/02/2020
Program Purpose :List Displayed using a report function
and using list function called .append to add a name
to the list before re running the report
"""

# initial list values
myNameList=["Jim", "John", "Jack", "Jenny", "Julie"]

# def function show length and display list elements
def Report():
    print("This list has",len(myNameList),"items")
    for i in range(len(myNameList)):# shows the list names
        print(myNameList[i])
        
    #identify the first list element at index 0         
    print("FIRST name is ", myNameList[0])
    #identify the first last element at index -1
    print("LAST name is ", myNameList[-1])
    

# runs function called report
Report()

# 1 line blank space
print()

# prompt user for new name
NewName=input("What is the new name :")

# add new name to myNameList using .append
myNameList.append(NewName)

# runs function called report
Report()

