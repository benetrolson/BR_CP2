from helper import *


def menu():
    gradebook = csv_to_dict("individual_projects/gradebook/docs/gradebook.csv")
    names = []
    print("Welcome to the gradebook! ")
    while True:
        check = int(choice_input(["1", "2", "3", "4", "5", "6"], "Do you want to \n1. Add New Student \n2. Add Grade to Student \n3. View Student Record \n4. View All Students \n5. Class Summary \n6. Exit \n> "))
        match check:
            case 1:
                name = input("What is the student's name? (Please capitalize correctly) \n> ")
                id_number = input("What is the id number of the student? ")
                year = int(choice_input(["9", "10", "11", "12"], "What is the grade of the student? "))
                gradebook.append({"name": name, "id": id_number, "year": year, "grades": [], "grade": 0})
            case 2:
                choice = choice_input(["1", "2"], "Would you rather find your student by their \n1. Name \n2. ID \n> ")
                if choice == "1":
                    key = "name"
                elif choice == "2":
                    key = "id"
                for i in gradebook:
                    names.append(i[key])
                if not names:
                    continue
                student = choice_input(names, f"What is the {key} of the student you are adding a grade to? ")
                grade = int_input("What is the student's new grade? ")
                for i in gradebook:
                    if i[key] == student:
                        i["grades"].append(grade)
                        i["grade"] = sum(i["grades"]) / len(i["grades"])
            case 3:
                choice = choice_input(["1", "2"], "Would you rather find your student by their \n1. Name \n2. ID \n> ")
                if choice == "1":
                    key = "name"
                elif choice == "2":
                    key = "id"
                for i in gradebook:
                    names.append(i[key])
                if not names:
                    continue
                student = choice_input(names, f"What is the {key} of the student you are viewing? ")
                for i in gradebook:
                    if i[key] == student:
                        print(f"Name: {i['name']} \nID: {i['id']} \nYear: {i['year']} \nGrades: ")
                        for grade in i["grades"].values():
                            print(grade)
                        print(f"Overall Grade: {i['grade']}")
            case 4:
                for i in gradebook:
                    print(f"Name: {i['name']} \nID: {i['id']} \nYear: {i['year']} \nGrades: ")
                    for grade in i["grades"].values():
                        print(grade)
                    print(f"Overall Grade: {i['grade']}")
            case 5:
                total = 0
                for i in gradebook:
                    total += i["grade"]
                print(f"The class average is {total / len(gradebook)}")
            case 6:
                break

menu()
