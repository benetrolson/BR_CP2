#BHR 2nd geometry calculator
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.circumference = 2 * radius * math.pi
        self.area = radius ** 2 * math.pi
    def display(self):
        print(f"Radius: {self.radius}, \nDiameter: {self.diameter}, \nCircumference: {self.circumference}, \nArea: {self.area}\n")

class Square:
    def __init__(self, length):
        self.length = length
        self.area = length ** 2
        self.diagonal = math.sqrt(length * 2)
        self.perimeter = length * 4
    def display(self):
        print(f"Length: {self.length}, \nArea: {self.area}, \nPerimeter: {self.perimeter}, \nDiagonal: {self.diagonal}\n")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.diagonal = math.sqrt(length + width)
        self.perimeter = length * 2 + width * 2
    def display(self):
        print(f"Length: {self.length}, \nWidth: {self.width}, \nArea: {self.area}, \nPerimeter: {self.perimeter}, \nDiagonal: {self.diagonal}\n")

class Triangle:
    def __init__(self, height, base_length):
        self.height = height
        self.base_length = base_length
        self.area = (base_length * height) / 2
        self.perimeter = base_length * 3
    def display(self):
        print(f"Length: {self.base_length}, \nHeight: {self.height}, \nArea: {self.area}, \nPerimeter: {self.perimeter}\n")


