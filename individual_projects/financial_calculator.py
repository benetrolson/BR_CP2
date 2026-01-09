# BHR 2nd financial calculator
import math

options = ["1. Savings Time Calculator", "2. Compound Interest Calculator", "3. Budget Allocator", "4. Sale Price Calculator", "5. Tip Calculator", "6. Quit"]

#Create a function for the menu
def menu(options):
    while True:
        print("Which option do you want to choose? ").strip()
        for i in options:
            print(options[i])
        check = input()
        if check == "1":
            savings()
            break
        elif check == "2":
            compound()
            break
        elif check == "3":
            budget()
            break
        elif check == "4":
            sale()
            break
        elif check == "5":
            tip()
            break
        elif check == "6":
            return "quit"
        else:
            print("You inputed an incorect input. Please input the number of the option that you want. ")
    
#Create a function for Savings Time Calculator
def savings():
    while True:
        print("Your options are: \n1. daily \n2. weekly \n3. monthly \n4. annually")
        check = input()
        if check == "1":
            time = "days"
            break
        if check == "2":
            time = "weeks"
            break
        if check == "3":
            time = "months"
            break
        if check == "4":
            time = "years"
            break
        else:
            print("You inputed an incorect input. Please input the number of the option that you want. ")
    while True:
        check = input()
#Create a function for Compound Interest Calculator

#Create a function for Budget Allocator

#Create a function for Sale Price Calculator

#Create a function for Tip Calculator

while True:
    check = menu()
    if check == "quit":
        break
