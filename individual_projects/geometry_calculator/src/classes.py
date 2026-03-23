#BHR 2nd geometry calculator
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.circumference = 2 * radius * math.pi
        self.area = radius ** 2 * math.pi
    def display(self):
        print(f"Shape: Circle, \nRadius: {self.radius}, \nDiameter: {self.diameter}, \nCircumference: {self.circumference}, \nArea: {self.area}\n")

class Square:
    def __init__(self, length):
        self.length = length
        self.area = length ** 2
        self.diagonal = length * math.sqrt(2)
        self.perimeter = length * 4
    def display(self):
        print(f"Shape: Square, \nLength: {self.length}, \nArea: {self.area}, \nPerimeter: {self.perimeter}, \nDiagonal: {self.diagonal}\n")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.diagonal = math.sqrt(length ** 2 + width ** 2)
        self.perimeter = length * 2 + width * 2
    def display(self):
        print(f"Shape: Rectangle, \nLength: {self.length}, \nWidth: {self.width}, \nArea: {self.area}, \nPerimeter: {self.perimeter}, \nDiagonal: {self.diagonal}\n")

class Triangle:
    def __init__(self, height, base_length):
        self.height = height
        self.base_length = base_length
        self.area = (base_length * height) / 2
        self.perimeter = base_length * 3
    def display(self):
        print(f"Shape: Triangle, \nLength: {self.base_length}, \nHeight: {self.height}, \nArea: {self.area}, \nPerimeter: {self.perimeter}\n")

class Cube:
    def __init__(self, length):
        self.length = length
        self.area = length ** 2 * 6
        self.volume = length ** 3
    def display(self):
        print(f"Shape: Cube, \nLength {self.length}, \nHeight: {self.length}, \nWidth: {self.length}, \nSurface Area: {self.area}, \nVolume: {self.volume}\n")

class Prism:
    def __init__(self, length, apothem, sides, height):
        self.length = length
        self.apothem = apothem
        self.height = height
        self.base_area = (length * sides * apothem)
        self.volume = (length * sides * apothem * height) / 2
        self.area = sides * height * length + length * sides * apothem
    def display(self):
        print(f"Shape: Cube, \nLength {self.length}, \nHeight: {self.height}, \nWidth: {self.apothem * 2}, \nBase Area {self.base_area}, \nSurface Area: {self.area}, \nVolume: {self.volume}\n") 

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = 4 * math.pi * radius ** 2
        self.volume = 4/3 * math.pi * radius ** 3
    def display(self):
        print(f"Shape: Sphere, \nRadius: {self.radius}, \nDiameter: {self.diameter}, \nSurface Area: {self.area}, \nVolume: {self.volume}\n")

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.diameter = radius * 2
        self.slant_length = math.sqrt(height ** 2 + radius ** 2)
        self.height = height
        self.area = math.pi * radius * self.slant_length + math.pi * radius ** 2
        self.volume = (math.pi * radius ** 2 * height) / 3
    def display(self):
        print(f"Shape: Cone, \nRadius: {self.radius}, \nDiameter: {self.diameter}, \nSlant Length: {self.slant_length}, \nHeight: {self.height}, \nSurface Area: {self.area}, \nVolume: {self.volume}\n")

class Pyramid:
    def __init__(self, apothem, height, sides):
        self.apothem = apothem
        self.height = height
        self.length = math.sqrt(height ** 2 + apothem ** 2)
        self.area = (sides * apothem * self.length) / 2 + (sides * apothem ** 2) / 2
        self.volume = (sides * apothem * height) / 6
    def display(self):
        print(f"Shape: Pyramid, \nApothem: {self.apothem}, \nHeight: {self.height}, \nSlant Length: {self.length}, \nSurface Area: {self.area}, \nVolume: {self.volume}\n")
        

def make_shape(shape_dict):
    if shape_dict["type"] == "square": return Square(int(shape_dict["length"]))
    elif shape_dict["type"] == "circle": return Circle(int(shape_dict["radius"]))
    elif shape_dict["type"] == "rectangle": return Rectangle(int(shape_dict["length"]), int(shape_dict["width"]))
    elif shape_dict["type"] == "triangle": return Triangle(int(shape_dict["height"]), int(shape_dict["length"]))
    elif shape_dict["type"] == "cube": return Cube(int(shape_dict["length"]))
    elif shape_dict["type"] == "prism": return Prism(int(shape_dict["length"]), int(shape_dict["radius"]), int(shape_dict["width"]), int(shape_dict["height"]))
    elif shape_dict["type"] == "sphere": return Sphere(int(shape_dict["radius"]))
    elif shape_dict["type"] == "cone": return Cone(int(shape_dict["radius"]), int(shape_dict["height"]))
    elif shape_dict["type"] == "pyramid": return Pyramid(int(shape_dict["apothem"]), int(shape_dict["height"]), int(shape_dict["sides"]))

