# File : Act04_proj5.py 
# Name : Michael Mathews  Date : 1/4/19
# Program Purpose : Convert Temperature
# Farenheit to Celsius,Celsius to Farenheit
# Show Boiling and Freezing Points for both

def fahr_to_Celsius():
    far = float(input("Please enter the temperature in Farenheit: "))
    cels = ((far-32)*(5/9))
    print (far,"Farenheit in Celsius is",cels,"degrees.")
    print()
def Celsius_to_Fahr():
    cel = float(input("Please enter the temperature in Celsius: "))
    farh = ((cel*(9/5)+32))
    print (cel,"Celsius in Farenheit is",farh,"degrees.")
    print()
def FreezeBoil():
    print ("The boling temperature is 100.0 C and 212 F.")
    print ("The freezing temperatures are 0.0 C and 32 F.")
    print()
menu = {}    # sets options for menu
menu['1']="- Convert Farenheit to Celsius" 
menu['2']="- Convert Celsius to Farenheit"
menu['3']="- Display the freezing and boiling points"
menu['0']="- Exit"

print(" Welcome to the Temperature Converter") # Welcomes User
print()                            # Leaves a 1 line space

while True: 
    options=menu.keys()            
    for entry in options:          # Displays Menu options
        print(entry, menu[entry])
    print()                           # Leaves a 1 line space
    selection=input("Please Select:") # Prompts user to select
    print()                           # Leaves a 1 line space
    if selection =='1': 
      fahr_to_Celsius()            # 1 select runs F to C

    elif selection == '2': 
      Celsius_to_Fahr()            # 2 select runs C to F

    elif selection == '3':
      FreezeBoil()                 # 3 Freezing-Boiling Display

    elif selection == '0':         # 0 Farewell User
      print("Thanks for use the Temperature convertor.  Stay Cool !")
      break
    else:                           # User Proofing
      print ("Unknown Option Selected!" )

