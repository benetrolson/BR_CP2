import random as rand
import csv

def csv_to_dict(path):
    try:
        with open(path, mode = 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            finished = []
            for line in reader:
                i = 0
                current_line = {}
                for column in header:
                    current_line[column] = line[i]
                    i += 1
                finished.append(current_line)
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e}. ")
    else: return finished
    return {}

def save_csv(path, dict):
    try:
        if not dict:
            return
        with open(path, mode = "w", newline="") as file:
            header = dict[0].keys()
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(dict)
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e}. ")
        

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
            return int(choice)
        elif choice in ["idk", "i don't know", "i dont know"]:
            return rand.randint(0, 10000000)
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
