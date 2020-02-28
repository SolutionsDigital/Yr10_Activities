# File : Act05_proj8.py
# Name : Michael Mathews
# Date : 1/4/19
""" Program Purpose :allow user to enter Data for lists and the calculate
Mode, median, min, max and Range
"""
# allow user to enter numbers for the list

myNumList = [5, 5, 2, 4, 4, 5]
select = "y"    # intialise variable called select


def Report():  # defining of function to give a report on List status
    # outputs number of list elements
    print("This list has", len(myNumList), "Numbers")
    for i in range(len(myNumList)):          # sets up loop displaying list elements
        print("Item", i, ":", myNumList[i])
    print()


def DeleteNum():
    deleteItem = int(input("What is the item number to delete:"))
    print("Item ", deleteItem, "deleted the colour ", myNumList[deleteItem])
    myNumList.pop(deleteItem)
    print()


def AddItem():
    print("You are about to ADD an item")
    print("------------------------------------")
    print()
    NewName = int(input("What is the new name :"))
    myNumList.append(NewName)
    print()
    print(myNumList[:])
    print()


def SortItems():
    myNumList.sort()
    print("list is sorted")


while select != "x" or "X":
    Report()
    print()
    print("press D to delete item")
    print("press A for adding item")
    print("press S for Sorting items")
    print("press X to EXIT")
    print()
    select = input("SELECT MENU LETTER  D or A or S or X : ")
    if select in ("D", "d"):
        DeleteNum()
    elif select in ("A", "a"):
        AddItem()
    elif select in ("S", "s"):
        SortItems()
    elif select in ("x", "X"):
        print("So Long")
        break
    else:
        print("------------------------------------")
        print("select ONLY   A  or  D  or  S  or X")
        print("------------------------------------")
