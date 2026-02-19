import random as rand

def choice_input(choices, prompt = ">"):
    while True:
        choice = input(prompt)
        if choice in choices:
            return choice
        else:
            print("That was an invalid input. Please try again. ")