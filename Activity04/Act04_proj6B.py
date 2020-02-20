# File : Act04_proj6.py 
# Name : Michael Mathews
# Date : 1/4/19
# Program Purpose : Checks if three numbers are pythorean numbers

def checkPythogoreanTheorem(a,b,c):
    if(((a**2)==((b**2)+(c**2))) or ((b**2)==((c**2)+(a**2))) or ((c**2)==((a**2)+(b**2)))):
        
        print("   |")
        print("   |  .")
        print(a," |    .", c)
        print("   |       .")
        print("   |          .")
        print("   --------------")
        print("         ",b)        
        return "Ohh yeah!"

    else:
        return "  Nope - wrong numbers."

counter = "y"
while True:
    if(counter == "n" or counter == "N"):
        break
    elif(counter == "y" or counter == "Y"):
        print()
        a,b,c=input("Enter three numbers seperated by a space: ").split()
        a,b,c=int(a),int(b),int(c)
        print("Are these Pythogorean Triplets? ")
        print()
        print(str(checkPythogoreanTheorem(a,b,c)))

        counter = input("Do you want to continue? (Y/N) ")
    else:
        print("Dude, it was a yes/no question.")
        counter = input("Do you want to continue? (Y/N) ")
