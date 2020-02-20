# File : Act06_proj1.py 
# Name :Michael Mathews
# Date :1/4/19
# Program Purpose Insert : Add Missing House Day at index 2
# --------------------------------------------------

houseList = ["Burchill", "Burling", "Fradgley", "Hobart","McIntosh", "Rapp", "Reeves"]
for i in range (len(houseList)):
    print(i, "-", houseList[i])

newIndex=int(input("What is the index value for the insert House :"))       
print()
newName=input("What is the name of the missing House :")

# Insert Day house at index 2 (third pos)
houseList.insert(newIndex, newName)
print(newName, "has been added at index number ",newIndex)
print()
for i in range (len(houseList)):
    print(i, "-", houseList[i])
