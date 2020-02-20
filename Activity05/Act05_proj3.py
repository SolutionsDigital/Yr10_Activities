"""
File : Act05_proj3.py 
Name : Michael Mathews     Date : 02/02/2020
Program Purpose : Report on list items showing 
first, second items + second last and last items
allow user to Delete a name from list using pop(index)
then re run the report
"""

# List of names sample for output
myNameList=["Jim", "John", "Jack", "Jenny", "Julie"]

# Function to show report on list details inc length
def Report():
    print("This list has",len(myNameList),"items")
    for i in range(len(myNameList)):
        print("Index",i,":",myNameList[i])
    print()    
    print("FIRST name is ", myNameList[0])
    print("Second name is ", myNameList[1])
    print("Second LAST name is ", myNameList[-2])
    print("LAST name is ", myNameList[-1])
    print("------------------------------------")

# function to enable item to be deleted or popped by item number
def DeleteNum():
    deleteItem=input("What is the index number to delete:")
    myNameList.pop(int(deleteItem))
    print("Item ",deleteItem, "deleted")
    print()

Report()    # runs report Function
DeleteNum()  # runs delete Function
Report()    # runs report Function
