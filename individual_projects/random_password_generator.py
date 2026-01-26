#BHR 2nd random password generator
import random

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
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    specials = "!@#$%^&*()¡™£¢∞§¶•ªº⁄€‹›ﬁﬂ‡°·‚œ∑´®†¥¨ˆøπåß∂ƒ¬…“‘«÷≥≤µ˜∫√ç≈ΩŒ„´‰ˇÁ¨ˆØ∏”’ÅÍÍÎÏ˝ÓÔÒÚÆ»`¸˛Ç◊ı˜Â¯˘¿Ω=-+_≠±—'\""
    while True:
        pool = ""
        password = []
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
            lower = input("Does the password need lowercase letters? (Y/N) \n").strip().title()
            pool, password = check(lower, lowercase, password, pool)
            if lower in ["Y", "N"]:
                break
        if len(password) >= length:
            print("This is too many additions for too short a password. Please try again. ")
            continue
        while True:
            upper = input("Does the password need uppercase letters? (Y/N) \n").strip().title()
            pool, password = check(upper, uppercase, password, pool)
            if upper in ["Y", "N"]:
                break
        if len(password) >= length:
            print("This is too many additions for too short a password. Please try again. ")
            continue
        while True:
            number = input("Does the password need numbers? (Y/N) \n").strip().title()
            pool, password = check(number, numbers, password, pool)
            if number in ["Y", "N"]:
                break
        if len(password) >= length:
            print("This is too many additions for too short a password. Please try again. ")
            continue
        while True:
            special = input("Does the password need special characters? (Y/N) \n").strip().title()
            pool, password = check(special, specials, password, pool)
            if special in ["Y", "N"]:
                break
        if len(password) >= length:
            print("This is too many additions for too short a password. Please try again. ")
            continue
        if pool == "":
            print("You must say yes to something. Please try again. ")
            continue
        print("Possible passwords: ")
        for i in range(4):
            password_ = password.copy()
            for _ in range(length - len(password)):
                password_.append(random.choice(pool))
            random.shuffle(password_)
            print(f"{i + 1}. {.join(password_)}")
        break
            
def check(input, characters, password, pool):
    match input:
        case "Y":
            pool += characters
            password.append(random.choice(characters))
            return pool, password, input
        case "N":
            return pool, password, input
        case _:
            print("Your input was not \"Y\" or \"N\". Please try again. ")
            return pool, password, input

