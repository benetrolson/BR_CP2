from helper import *


def menu():
    gradebook = csv_to_dict("individual_projects\\gradebook\\docs\\gradebook.csv")
    names = []
    while True:
        print("Welcom to the gradebook! ")
        check = choice_input(["1", "2", "3", "4", "5", "6", "7"], "Do you want to \n1. Create a new account[1] Add New Student \n2. Add Grade to Student \n3. View Student Record \n4. View All Students \n5. Class Summary \n6. Exit")
        match check:
            case 1:
                name = input("What is the student's name? (Please capitalize correctly) \n> ")
                id_number = input("What is the id number of the student? ")
                year = int(choice_input(["9", "10", "11", "12"], "What is the grade of the student? "))
                gradebook.append({"name": name, "id": id_number, "year": year, "grades": {}, "grade": 0})
            case 2:
                choice = choice_input(["1", "2"], "Would you rather find your student by their ")
                for i in gradebook:
                    names.append(i["name"])
                name = choice_input(names, "What is the name of the student you are adding a grade to? ")
            case 6:
                break


menu()
