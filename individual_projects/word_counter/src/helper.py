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

def txt_reader(path):
    try:
        with open(path) as file:
            return file
    except Exception as e:
        print(f"You had an {e}. ")
