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
        amount = input("How much money do you want to save up? ").strip()
        if amount.isdigit():
            amount = int(amount)
            break
        print("You did not input a number. Please try again. ")
    while True:
        print("Your options are: \n1. daily \n2. weekly \n3. monthly \n4. annually")
        time = input().strip()
        if time == "1":
            time = "days"
            break
        if time == "2":
            time = "weeks"
            break
        if time == "3":
            time = "months"
            break
        if time == "4":
            time = "years"
            break
        else:
            print("You inputed an incorect input. Please input the number of the option that you want. ")
    while True:
        deposit = input("How much are you inputing each time? ").strip()
        if check.isdigit():
            deposit = int(deposit)
            break
        print("You did not input a number. Please try again. ")
    print(f"It will take {amount/deposit} {time} to save up to ${amount}. ")
    
#Create a function for Compound Interest Calculator
def compound():
    while True:
        start = input("What will be your starting amount? ").strip()
        if start.isdigit():
            start = int(start)
            break
        print("You did not input a number. Please try again. ")
    while True:
        rate = input("What will the interest rate be? ").strip()
        if rate.isdigit():
            rate = 1 + ((int(rate))/100)
            break
        print("You did not input a number. Please try again. ")
    while True:
        year = input("How many years will you leave the money alone? ").strip()
        if year.isdigit():
            year = int(year)
            break
        print("You did not input a number. Please try again. ")
    final = start
    for i in range(year):
        final = rate * final
    print(f"At the end of {year} years you will have ${final}. ")

#Create a function for Budget Allocator
def 

#Create a function for Sale Price Calculator

#Create a function for Tip Calculator

while True:
    check = menu()
    if check == "quit":
        break
