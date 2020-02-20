# Act06_proj4.py 
# Name :Michael Mathews
# Date :1/4/19
""" Program Purpose : Deleting from List using del Function
""" 

myPetList=["Dog", "Cat", "Bird", "Horse", "Cow"]
# Defines a function to show the list
def showList():
    print()
    print("This list of Pets has ", len(myPetList)  ,"items")
    # lists the items in the list
    for i in range(len(myPetList)):
        print(i,"-", myPetList[i])
    print()    

# runs the function "showList"
showList()

# allows user to select index value to delete from the list
deleteItem=int(input("What is the Item number to delete:"))
# allows user to see the item to be deleted from the list
print(deleteItem,"-",myPetList[deleteItem]," has been deleted from the List")
# deletes index value item from the list
del myPetList[deleteItem]

# runs the function "showList"
showList()
