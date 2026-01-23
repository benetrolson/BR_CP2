#BHR 2nd random password generator

def main():
    while True:
        check = input("Do you want to: \n1. Make a new passcode \n2. Quit \n").strip()
        if check == "1":
            create()
        elif check == "2":
            break
        else:
            print("That was not a valid option. Please try again. ")

def create():
    while True:
        length = input("How long does the password need to be? ").strip()
        if length.isdigit():
            length = int(length)
            if length <= 0:
                print("Your input was too small. Please try again. ")
            else:
                break
        else:
            print("Your input was not a number. Please try again. ")
    while True:
        lower = input("Does the passwird need lowercase letters? (Y/N) \n").strip().title()
        if lower == "Y" or lower == "N":
            break
        print("Your input was not \"Y\" or \"N\". Please try again. ")
    while True:
        upper = input("Does the passwird need uppercase letters? (Y/N) \n").strip().title()
        if upper == "Y" or upper == "N":
            break
        print("Your input was not \"Y\" or \"N\". Please try again. ")
    while True:
        number = input("Does the password need numbers? (Y/N) \n").strip().title()
        if number == "Y" or number == "N":
            break
        print("Your input was not \"Y\" or \"N\". Please try again. ")

