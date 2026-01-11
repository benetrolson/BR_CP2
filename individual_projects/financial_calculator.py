# BHR 2nd financial calculator
import math

options = ["1. Savings Time Calculator", "2. Compound Interest Calculator", "3. Budget Allocator", "4. Sale Price Calculator", "5. Tip Calculator", "6. Quit"]

#Create a function for the menu
def menu(options):
    while True:
        print("Which option do you want to choose? ")
        for i in options:
            print(i)
        check = input().strip()
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
            return check
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
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit <= 0:
                print("Your deposit cannot be 0 or lower. ")
            else:
                break
        else:
            print("You did not input a number. Please try again. ")
    print(f"It will take {math.ceil(amount/deposit)} {time} to save up to ${amount}. ")
    
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
            rate = int(rate)
            if rate > 100:
                print("Your interest rate is too big. Please try again. ")
            elif rate < 0:
                print("Your interest rate is too small. Please try again. ")
            else:
                rate = 1 + rate/100
                break
        else:
            print("You did not input a number. Please try again. ")
    while True:
        year = input("How many years will you leave the money alone? ").strip()
        if year.isdigit():
            year = int(year)
            break
        print("You did not input a number. Please try again. ")
    print(f"At the end of {year} years you will have ${start * (rate ** year)}. ")

#Create a function for Budget Allocator
def budget():
    def category_solver():
        categories = []
        for i in range(amount):
            while True:
                category = input(f"Category {i + 1} will be: ").strip()
                if not category in categories:
                    break
                print("You have already inputted that. Please try again. ")
            categories.append(category)
        return categories
    def percentage_solver():
        percentages = []
        for i in categories:
            while True:
                total = 0
                percent = input(f"What percent are you dedicating to {i}? ").strip()
                if percent.isdigit():
                    percent = int(percent)
                    for r in percentages:
                        total += r
                    if total + percent > 100:
                        print("You have gone over 100. Please restart. ")
                        return None
                    elif total + percent == 100 and i == categories[-1]:
                        percentages.append(percent)
                        return percentages
                    elif total + percent == 100:
                        print("You have reached 100 before you were supposed to. Please restart. ")
                        return None
                    elif i == categories[-1]:
                        print("You have run out of categories before getting to 100. Please restart. ")
                        return None
                    elif percent <= 0:
                        print("Your percent is too low. Please try again. ")
                    else:
                        percentages.append(percent)
                        break
                else:
                    print("You did not input a number. Please try again. ")
    while True:
        amount = input("How many budget categories will you have? ").strip()
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("You didn't have enough categories. Please try again. ")
            else:
                break
        else:
            break
    while True:
        income = input("What is your monthly income? ").strip()
        if income.isdigit():
            income = int(income)
            if income > 0:
                break
            print("Your income is too low. Please try again. ")
        print("You did not input a number. Please try again. ")
    categories = category_solver()
    while True:
        percentages = percentage_solver()
        if percentages != None:
            break
    for i in range(len(categories)):
        print(f"{categories[i]}: ${income * (percentages[i] / 100)}")

#Create a function for Sale Price Calculator
def sale():
    while True:
        initial = input("How much did this item originally cost? ").strip()
        if initial.isdigit():
            initial = int(initial)
            if initial > 0:
                break
            print("Your input was too small. Please try again. ")
        else:
            print("You did not input a number. Please try again. ")
    while True:
        discount = input("What percent is the discount? ").strip()
        if discount.isdigit():
            discount = int(discount)
            if discount <= 0:
                print("Your discount is too small. Please try again. ")
            elif discount >= 100:
                print("Your discount is too big. Please try again. ")
            else:
                break
        else:
            print("You did not input a number. Please try again. ")
    print(f"Your discounted item now costs ${initial * ((100 - discount)/100)}")

#Create a function for Tip Calculator
def tip():
    while True:
        bill = input("How much is the bill? ").strip()
        if bill.isdigit():
            bill = int(bill)
            if bill > 0:
                break
            print("Your bill is too small. Please try again. ")
        else:
            print("You did not input a number. Please try again. ")
    while True:
        percent = input("What is the percent of the tip that you are giving? ")
        if percent.isdigit():
            percent = int(percent)
            if percent <= 0:
                print("Your tip is too small. Please try again. ")
            elif percent >= 100:
                print("Your tip is too big. Please try again. ")
            else:
                break
        else:
            print("You did not input a number. Please try again. ")
    print(f"The tip amount is ${(percent/100) * bill} and your total is ${(1 + (percent/100)) * bill}. ")

while True:
    check = menu(options)
    if check == "6":
        break
