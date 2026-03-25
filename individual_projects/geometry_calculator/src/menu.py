#Geometry Calculator

def main():
    shapes = csv_to_dict("individual_projects/geometry_calculator/docs/geometry_calculator.csv")
    while True:
        print(f"Welcome to the geometry calculator! ")
        check = choice_input(["1", "2", "3", "4", "5"], "What do you want to do? \n1. Create new shape \n2. View all shapes \n3. View specific shape \n4. Formula guide \n5. Quit \n> ")
        match check:
            case "1":
                choice = choice_input(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], "What shape do you want to create? \n1. Square \n2. Circle \n3. Rectangle \n4. Triangle \n5. Cube \n6. Prism \n7. Sphere \n8. Cone \n9. Pyramid \n10. Exit \n> ")
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
                    case "5":
                        length = int_input("What will the length of the cube be? ")
                        shapes.append({
                            "type": "cube",
                            "length": length,
                            "width": "",
                            "height": "",
                            "radius": ""
                        })
                    case "6":
                        length = int_input("What will the length of a side be? ")
                        apothem = int_input("What will the length of the apothem be? ")
                        height = int_input("What will the height of the prism be? ")
                        sides = int_input("How many sides will there be? ")
                        shapes.append({
                            "type": "prism",
                            "length": length,
                            "width": sides,
                            "height": height,
                            "radius": apothem
                        })
                    case "7":
                        radius = int_input("What will the radius of the sphere be? ")
                        shapes.append({
                            "type": "sphere",
                            "length": "",
                            "width": "",
                            "height": "",
                            "radius": radius
                            })
                    case "8":
                        radius = int_input("What will the radius of the cone be? ")
                        height = int_input("What will the height of the cone be? ")
                        shapes.append({
                            "type": "cone",
                            "length": "",
                            "width": "",
                            "height": height,
                            "radius": radius
                            })
                    case "9":
                        apothem = int_input("What will the length of the apothem be? ")
                        height = int_input("What will the height of the pyramid be? ")
                        sides = int_input("How many sides will there be? ")
                        shapes.append({
                            "type": "pyramid",
                            "length": "",
                            "width": "",
                            "height": height,
                            "radius": apothem,
                            "sides": sides
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
                if choice == "q": continue
                make_shape(shapes[int(choice) - 1]).display()
            case "4":
                print("\nSquare:\nArea = side^2\nPerimeter = 4*side\nDiagonal = side*(2^0.5)\n\nCircle:\nArea = π*radius^2\nCircumference = 2*π*radius\n\nRectangle:\nArea = width*height\nPerimeter = 2*(width + height)\nDiagonal = (width^2 + height^2)^0.5\n\nTriangle:\nArea = 0.5*base*height\nPerimeter = a + b + c  # if all three sides are known\n\nSphere:\nVolume = (4/3)*π*radius^3\nSurface Area = 4*π*radius^2\n\nCube:\nVolume = side^3\nSurface Area = 6*side^2\nDiagonal = side*(3^0.5)\n\nPrism (regular base):\nVolume = (1/2)*n*side*apothem*height\nSurface Area = n*side*(height + apothem)\n\nCone:\nVolume = (1/3)*π*radius^2*height\nSurface Area = π*radius*(radius + slant_height)\nSlant Height = (radius^2 + height^2)^0.5\n\nPyramid (regular base):\nVolume = (1/6)*n*side*apothem*height\nSurface Area = (1/2)*n*side*(apothem + slant_height)\nSlant Height = (height^2 + apothem^2)^0.5")
            case "5":
                break
        save_csv("individual_projects/geometry_calculator/docs/geometry_calculator.csv", shapes)
