# BHR 2nd portable dinner (pet) simulator
from helper import *
from classes import *

def main():
    #while True:
        print(f"Welcome to the geometry calculator! \nYou have these shapes already. ")
        check = choice_input(["1", "2", "3", "4", "5"], "What do you want to do? \n1. Create new shape \n2. View all shapes \n3. View specific shape \n4. Formula guide \n5. Quit \n> ")
        match check:
            case "1":
                choice = choice_input(["1", "2", "3", "4"], "What shape do you want to create? \n1. Square \n2. Circle \n3. Rectangle \n4. Triangle \n> ")
                match choice:
                    case "1":
                        length = int_input("What will the length of the square? ")
                        square = Square(length)



main()