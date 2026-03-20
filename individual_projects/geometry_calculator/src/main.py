# BHR 2nd geometry calculator
from helper import *
from classes import *

def main():
    shapes = csv_to_dict("individual_projects/geometry_calculator/docs/geometry_calculator.csv")
    while True:
        print(f"Welcome to the geometry calculator! ")
        check = choice_input(["1", "2", "3", "4", "5"], "What do you want to do? \n1. Create new shape \n2. View all shapes \n3. View specific shape \n4. Formula guide \n5. Quit \n> ")
        match check:
            case "1":
                choice = choice_input(["1", "2", "3", "4", "5"], "What shape do you want to create? \n1. Square \n2. Circle \n3. Rectangle \n4. Triangle \n5. Exit \n> ")
                match choice:
                    case "1":
                        length = int_input("What will the length of the square be? ")
                        shapes.append({
                            "type": "square",
                            "length": length,
                            "width": "",
                            "height": "",
                            "radius": ""
                            })
                    case "2":
                        radius = int_input("What will the radius of the circle be? ")
                        shapes.append({
                            "type": "circle",
                            "length": "",
                            "width": "",
                            "height": "",
                            "radius": radius
                            })
                    case "3":
                        length = int_input("What will the length of the rectangle be? ")
                        width = int_input("What will the width of the rectangle be? ")
                        shapes.append({
                            "type": "rectangle",
                            "length": length,
                            "width": width,
                            "height": "",
                            "radius": ""
                            })
                    case "4":
                        height = int_input("What will the height of the triangle be? ")
                        length = int_input("What will the length of the triangle be? ")
                        shapes.append({
                            "type": "triangle",
                            "length": length,
                            "width": "",
                            "height": height,
                            "radius": ""
                            })
            case "2":
                if not shapes:
                    continue
                for i, shape in enumerate(shapes):
                    print(f"{i+1}: ")
                    shape = make_shape(shape)
                    shape.display()
            case "3":
                if not shapes:
                    continue
                options = []
                for i in range(len(shapes)):
                    options.append(str(i + 1))
                choice = choice_input(options, "What is the number of the shape you want to look at? (Choose 'q' if you want to quit). \n> ")
                make_shape(shapes[int(choice) - 1]).display()
            case "4":
                print("Square:\nArea = side^2\nPerimeter = 4*side\nDiagonal = side*(2^0.5)\n\nCircle:\nArea = π*radius^2\nCircumference = 2*π*radius\n\nRectangle:\nArea = width*height\nPerimeter = 2*(width + height)\nDiagonal = (width^2 + height^2)^0.5\n\nTriangle:\nArea = 0.5*base*height\nPerimeter = a + b + c  # if all three sides are known")
            case "5":
                break
        save_csv("individual_projects/geometry_calculator/docs/geometry_calculator.csv", shapes)

main()