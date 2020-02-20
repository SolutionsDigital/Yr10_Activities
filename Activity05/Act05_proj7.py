# File : Act05_proj4.py 
# Name : Michael Mathews
# Date : 1/4/19
# Program Purpose :Delete names from list
# --------------------------------------------------

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
