import random as rand

def choice_input(choices, prompt = ">"):
    while True:
        choice = input(prompt).lower().strip()
        if choice in choices:
            return choice
        elif choice in ["idk", "i don't know", "i dont know"]:
            return rand.choice(choices)
        else:
            print("That was an invalid input. Please try again. ")

def int_input(choices, prompt = ">"):
    while True:
        choice = input(prompt).strip()
        if choice.isdigit():
            choice = int(choice)
            if choice in choices:
                return choice
            else:
                print("That was not a choice. Please try again. ")
        elif choice in ["idk", "i don't know", "i dont know"]:
            return rand.choice(choices)
        else:
            print("That is not a number. Please try again. ")

def txt_reader(path):
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError:
        print("The file was not found. ")
    except Exception as e:
        print(f"You had an {e}. ")
        return ""

def txt_saver(path, content):
    try:
        with open(path, "w") as document:
            document.write(content)
    except FileNotFoundError:
        print("The file was not found. ")
    except Exception as e:
        print(f"You had an {e}. ")
