from helper import *

class Student:
    def __init__(self, name, id_number, year, grades):
        self.name = name
        self.id = id_number
        self.year = year
        self.grades = grades
        self.grade = sum(grades) / len(grades) if grades else 0
        self.letter_grade = self.get_letter_grade()
        self.academic_standing = self.get_academic_standing(self.grade)
    def get_letter_grade(self):
        if self.grade >= 90:
            return "A"
        elif self.grade >= 80:
            return "B"
        elif self.grade >= 70:
            return "C"
        elif self.grade >= 60:
            return "D"
        else:
            return "F"
    def get_academic_standing(self, grade):
        if grade >= 90: return "Honor Roll"
        elif grade >= 80: return "Average"
        else: return "Needs Improvement"
    def add_grade(self, grade):
        self.grades.append(grade)
        self.grade = sum(self.grades) / len(self.grades)
        self.letter_grade = self.get_letter_grade()
        self.academic_standing = self.get_academic_standing(self.grade)
    def view_student(self):
        print(f"Name: {self.name} \nID: {self.id} \nYear: {self.year} \nGrades: ")
        for grade in self.grades:
            print(grade)
        print(f"Overall Grade: {self.grade} \nLetter Grade: {self.letter_grade} \nAcademic Standing: {self.academic_standing}")

class Gradebook:
    def __init__(self, students = None):
        self.students = students if students else []
    def add_student(self, student):
        for s in self.students:
            if s.id.strip() == student.id.strip():
                print("A student with this ID already exists.")
                return
        self.students.append(student)
    def view_student(self, value, key):
        for i in self.students:
            if getattr(i, key) == value:
                i.view_student()
                return
        print("Student not found. ")
    def view_all_students(self):
        for i in self.students:
            i.view_student()
    def class_summary(self):
        if not self.students:
            print("There are no students in the gradebook. ")
            return
        total = 0
        for i in self.students:
            total += i.grade
        print(f"The class average is {total / len(self.students)}")
    def class_statistics(self):
        if not self.students:
            print("There are no students in the gradebook. ")
            return
        grades = [i.grade for i in self.students]
        print(f"Class Average: {sum(grades) / len(grades)} \nHighest Grade: {max(grades)} \nLowest Grade: {min(grades)}")
