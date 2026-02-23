from time_finder import *
from word_counter import *
from helper import *
from document_checker import *

def main():
    path = input("What is the path of the file you will be editing? ")
    while True:
        check = choice_input(["1", "2", "3", "4"], "Do you want to: \n1. Find the word count \n2. View the document \n3. Edit the document \n4. Exit \n> ")
        if check == "1":
            print(f"Word count: {word_counter(remove_word_count(txt_reader(path)))}")
        elif check == "2":
            view(path)
        elif check == "3":
            edit(path)
        elif check == "4":
            break

main()
