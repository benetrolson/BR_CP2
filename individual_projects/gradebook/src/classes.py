from helper import *

class Student:
    def __init__(self, name, id_number, year, grades):
        self.name = name
        self.id = id_number
        self.year = year
        self.grades = grades
        self.grade = sum(grades) / len(grades) if grades else 0

class Gradebook:
    def __init__(self, students = None):
        self.students = students if students else []
    def add_student(self, student):
        self.students.append(student)
    def add_grade(self, student, grade):
        for i in self.students:
            if i.name == student.name and i.id == student.id:
                i.grades.append(grade)
                i.grade = sum(i.grades) / len(i.grades)
    def view_student(self, value, key):
        for i in self.students:
            if getattr(i, key) == value:
                print(f"Name: {i.name} \nID: {i.id} \nYear: {i.year} \nGrades: ")
                for grade in i.grades:
                    print(grade)
                print(f"Overall Grade: {i.grade}")
    def view_all_students(self):
        for i in self.students:
            print(f"Name: {i.name} \nID: {i.id} \nYear: {i.year} \nGrades: ")
            for grade in i.grades:
                print(grade)
            print(f"Overall Grade: {i.grade}")
    def class_summary(self):
        total = 0
        for i in self.students:
            total += i.grade
        print(f"The class average is {total / len(self.students)}")
