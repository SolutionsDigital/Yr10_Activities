"""
File : Act05_proj6.py   Name : Michael Mathews  Date : 02/02/2020
Program Purpose :Adjust elements of a colour List
including the Adding , Deleting and sorting of Elements
"""
# List of names sample for output

myColourList=["Green", "Red", "Black", "Blue", "Orange", "Purple"]
select="y"    # intialise variable called select
def Report():     #  defining of function to give a report on List status
    print("This list has",len(myColourList),"items")    # outputs number of list elements
    for i in range(len(myColourList)):          # sets up loop displaying list elements
        print("Item",i,":",myColourList[i])
    print()                                     
    print("FIRST Item is ", myColourList[0])
    print("Second Item is ", myColourList[1])
    print("Second LAST Item is ", myColourList[-2])
    print("LAST Item is ", myColourList[-1])
    print("------------------------------------")

def DeleteNum():
    deleteItem=int(input("What is the item number to delete:"))  
    print("Item ",deleteItem, "deleted the colour ", myColourList[deleteItem] )
    myColourList.pop(deleteItem)
    print()

def AddItem():
    print("You are about to ADD an item")
    print("------------------------------------")
    print()
    NewName=input("What is the new name :")
    myColourList.append(NewName)
    print()
    print(myColourList[:])
    print()

def SortItems():
    myColourList.sort()
    print()
 
while select != "x" or "X":
    Report()
    print()
    print("press D to delete item")
    print("press A for adding item")
    print("press S for Sorting items")
    print("press X to EXIT")
    print()
    select=input("SELECT MENU LETTER  D or A or S or X : ")
    if select in ("D","d"):
        DeleteNum()
    elif select in ("A","a"):
        AddItem()
    elif select in ("S","s"):
        SortItems()
    elif select in ("x","X"):
        print("So Long")
        break
    else:
        print("------------------------------------")
        print("select ONLY   A  or  D  or  S  or X")
        print("------------------------------------")
