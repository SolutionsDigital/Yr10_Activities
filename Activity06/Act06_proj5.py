# File : Act06_proj5.py 
# Name :Michael Mathews
# Date :1/4/19
""" Program Purpose : Deleting items using
Del index   or   Remove for item Name
"""
myCountriesList=["Greenland", "Russia", "Brazil", "England", "Australia", "Japan", "France"]
userSelection ="y"

def showOptions():
    print("----------------------------------")
    print("Press D - To delete a Country by Number  ")
    print("Press R - To remove a Country by Name")
    print("Press X - To EXIT")
    print("----------------------------------")
    print()
    
def Report():
    print()
    print("There are",len(myCountriesList), "Countries in this list. ",)
    print()
    for i in range (len(myCountriesList)):
        print(i+1, " - ", myCountriesList[i])
    print()

def removeCountry():
    print()
    removeThisCountry=input("Type the Name of the Country to remove: ")
    myCountriesList.remove(removeThisCountry)
    print()
    print(removeThisCountry, "has been removed")
    print("-------------------------------")
    
def popCountry():
    print()
    popThisCountry=int(input("Type the Number of the Country to deleted: "))
    popThisCountry=popThisCountry-1
    if popThisCountry < 0:
        print("Selected Number out of range")
    elif popThisCountry > len(myCountriesList):
        print("Selected Number out of range")
    else:
        print()
        print(popThisCountry+1, '-', myCountriesList[popThisCountry], "has been Deleted")
        myCountriesList.pop(popThisCountry)
        print("-------------------------------")

while userSelection != "X" or "x":
    Report()
    showOptions()
    userSelection=input("Select the Letter Option :")
    if userSelection in ("D","d"):
        popCountry()
    elif userSelection in ("R","r"):
        removeCountry()
    elif userSelection in ("S","s"):
        sortCountries()
    elif userSelection in ("X","x"):
        break
    else:(" Try a valid Character of D  R  S  or X ")
        
print("See you next time")
