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
                    if "," in line[i]:
                        line[i] = strlistconvert(line[i])
                        for value in line[i]:
                            if ":" in value:
                                line[i] = listdictconvert(line[i])
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
            for key, value in dict.items():
                if isinstance(value, (list, dict)):
                    dict[key] = str(value)
            header = dict[0].keys()
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(dict)
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e}. ")
        

def choice_input(choices, prompt = ">"):
    while True:
        choice = input(prompt)
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

def strlistconvert(string):
    strlist = []
    tempstr = ""
    for char in string:
        if char != ",":
            tempstr = f"{tempstr}"+f"{char}"
        else:
            strlist.append(tempstr)
            tempstr = ""
    return strlist

def listdictconvert(listitem):
    dictversion = {}
    for item in listitem:
        keypair = item.split(":")
        dictversion[keypair[0]] = keypair[1]
    return dictversion
