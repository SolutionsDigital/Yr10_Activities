# Act06_proj6.py 
# Name : Michael Mathews
# Date :  1 /4 / 19
"""Program Purpose : Allow a user to maintain a list of Countries that
can be listed, added to and / or   deleted from and or Sorted
"""

myCountriesList=["Greenland", "Russia", "Brazil", "England", "Australia", "Japan", "France"]
userSelection ="y"

def showOptions():
    print("----------------------------------")
    print("Press A - To add a Country  ")
    print("Press D - To delete a Country by Number  ")
    print("Press R - To remove a Country by Name")
    print("Press U - To Reverse Sort Countries z - a    ")
    print("Press S - To Sort Countries a - z    ")
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
    
def addCountry():
    print()
    newCountry=input("What is the new name :")
    myCountriesList.append(newCountry)

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

def sortCountries():
    myCountriesList.sort()
    print("sorted")

def reverseCountries():
    myCountriesList.reverse()
    print("Reverse sorted")

while userSelection != "X" or "x":
    Report()
    showOptions()
    userSelection=input("Select the Letter Option :")
    if userSelection in ("A","a"):
        addCountry()
    if userSelection in ("D","d"):
        popCountry()
    if userSelection in ("R","r"):
        removeCountry()
    if userSelection in ("S","s"):
        sortCountries()
    if userSelection in ("U","u"):
        reverseCountries()
    if userSelection in ("X","x"):
        break
        
print("See you next time")
