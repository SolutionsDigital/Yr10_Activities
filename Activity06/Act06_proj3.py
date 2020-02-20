# File : Act06_proj3.py 
# Name :Michael Mathews
# Date :1/4/19
# Program Purpose :
# --------------------------------------------------

# Initial list provided
myNumberList = [4,7,2,9,5,3]
#  List of extra numbers provided
extraNumbers = [8,1,13,11]

# Print out current list with
for i in range (len(myNumberList)):
    print("index -",i, "is", myNumberList[i])
print()
# Print out the list : length , max and min
print("The number of items in list is",len(myNumberList))
print ("Maximum is ",max(myNumberList))
print ("Minimum is ",min(myNumberList))
print()
myNumberList.extend(extraNumbers)

myNumberList.sort()
myNumberList.reverse()
print("The new List of reverse sorted Values looks like this")
for i in range (len(myNumberList)):
    print("index -",i, "is ", myNumberList[i])
print()
# Print out the new list : length , max and min
print("The number of items in list is",len(myNumberList))
print ("Maximum is ",max(myNumberList))
print ("Minimum is ",min(myNumberList))
