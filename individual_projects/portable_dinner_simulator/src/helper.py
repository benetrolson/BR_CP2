import random as rand
import csv

def csv_to_dict(path, mode = 'r'):
    try:
        with open(path):
            pass
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e}. ")
    else: 
        with open(path, mode = 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            users = []
            for line in reader:
                users.append(
                    {
                        header[0]: line[0],
                        header[1]: line[1]
                    }
                )

def csv_to_dictionary(file_path):
    try:
        with open(file_path, mode = 'r'):
            pass
    except FileNotFoundError:
        print('An error was encountered! Invalid file path.')
        return {'error': FileNotFoundError}
    except Exception as e:
        print(f"An unexpected error was encountered: {e}. ")
        return {'error': e}
    #create empty list
    finished = []
    #open csv file in read mode
    with open(file_path, mode = 'r') as file:
        #create csv reader
        reader = csv.reader(file)
        #get first line in reader
        header = next(reader)
        #loop through reader:
        for line in reader:
            #create empty dictionary
            current_line = {}
            #set iterator to 0
            i = 0
            #loop through first line:
            for column in header:
                #create new line in the dictionary with the first line value as the key and the respective line value as the value
                current_line[column] = line[i]
                i += 1
            #add dictionary to list
            finished.append(current_line)
        return finished


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
