import random as rand
import csv

def csv_to_dict(path):
    try:
        with open(path):
            pass
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e}. ")
    else: 
        with open(path, mode = 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            finished = []
            for line in reader:
                i = 0
                current_line = {}
                for column in header:
                    current_line[column]
                    i += 1
                finished.append(current_line)
        return finished
    return {}

def choice_input(choices, prompt = ">"):
    while True:
        choice = input(prompt).lower().strip()
        if choice in choices:
            return choice
        elif choice in ["idk", "i don't know", "i dont know"]:
            return rand.choice(choices)
        else:
            print("That was an invalid input. Please try again. ")

def int_input(prompt = ">"):
    while True:
        choice = input(prompt).lower().strip()
        if choice.isdigit():
            return choice
        elif choice in ["idk", "i don't know", "i dont know"]:
            return rand.randint(0, 10000000)
        else:
            print("That was an invalid input. Please try again. ")

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

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result
