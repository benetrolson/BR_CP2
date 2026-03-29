from helper import *
from classes import *

def menu():
    dictionary = csv_to_dict("individual_projects/gradebook/docs/gradebook.csv")
    gradebook = Gradebook()
    for i in dictionary:
        grades = i["grades"]
        if isinstance(grades, str): grades = strlistconvert(grades)
        if not isinstance(grades, list): grades = []
        gradebook.add_student(Student(i["name"], i["id"], i["year"], grades))
    print("Welcome to the gradebook! ")
    while True:
        names = []
        check = int(choice_input(["1", "2", "3", "4", "5", "6"], "Do you want to \n1. Add New Student \n2. Add Grade to Student \n3. View Student Record \n4. View All Students \n5. Class Summary \n6. Exit \n> "))
        match check:
            case 1:
                name = input("What is the student's name? (Please capitalize correctly) \n> ")
                id_number = input("What is the id number of the student? ")
                year = int(choice_input(["9", "10", "11", "12"], "What is the grade of the student? "))
                check = int_input("How many grades do you want to add for the student? ")
                grades = []
                for _ in range(check):
                    grade = int_input("What is the student's grade? ")
                    grades.append(grade)
                gradebook.add_student(Student(name, id_number, year, grades))
            case 2:
                choice = choice_input(["1", "2"], "Would you rather find your student by their \n1. Name \n2. ID \n> ")
                if choice == "1":
                    key = "name"
                elif choice == "2":
                    key = "id"
                for i in gradebook.students:
                    names.append(getattr(i, key))
                if not names:
                    continue
                student = choice_input(names, f"What is the {key} of the student you are adding a grade to? ")
                grade = int_input("What is the student's new grade? ")
                for i in gradebook.students:
                    if getattr(i, key) == student:
                        i.grades.append(grade)
                        i.grade = sum(i.grades) / len(i.grades)

            case 3:
                choice = choice_input(["1", "2"], "Would you rather find your student by their \n1. Name \n2. ID \n> ")
                if choice == "1":
                    key = "name"
                elif choice == "2":
                    key = "id"
                for i in gradebook.students:
                    names.append(getattr(i, key))
                if not names:
                    continue
                student = choice_input(names, f"What is the {key} of the student you are viewing? ")
                gradebook.view_student(student, key)
            case 4:
                if not gradebook.students:
                    print("There are no students in the gradebook. ")
                    continue
                gradebook.view_all_students()
            case 5:
                gradebook.class_summary()
            case 6:
                break
        save_csv("individual_projects/gradebook/docs/gradebook.csv", [vars(student) for student in gradebook.students])

menu()
