from time_finder import *
from word_counter import *
from helper import *
from document_checker import *

def main():
    while True:
        check = choice_input(["1", "2", "3", "4"], "Do you want to: \n1. Find the word count \n2. View the document \n3. Edit the document \n4. Exit \n> ")
        if check == "1":
            word_counter()
        if check == "2":
            view()
        if check == "3":
            edit()
        if check == "4":
            break

main()
