#BHR 2nd fractal generator
from helper import *
import turtle as t
from fractal_generator import *

#Create a main loop
def main():
    colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white", "bisque"]
    while True:
        t.clearscreen()
        quantity = int_input([1, 2, 3, 4, 5], "What do you want the recursion depth to be? (1-5). ")
        color = choice_input(colors, "What do you want the color of the fractal to be? ")
        background_color = choice_input(colors, "What do you want the color of the background to be? ")
        fractal = choice_input(["sierpinski", "sierpinski triangle", "koch", "koch snowflake"], "What fractal do you want to make? ")
        t.tracer(0, 0)
        t.color(color)
        t.bgcolor(background_color)
        if fractal in["sierpinski", "sierpinski triangle"]:
            t.teleport((-250/2**((quantity-5)*-1)), (-250/2**((quantity-5)*-1)))
            sierpinski(quantity)
        elif fractal in ["koch", "koch snowflake"]:
            t.teleport(-350, -200)
            t.left(90)
            for i in range(6):
                koch(400, quantity)
                t.right(60)
        t.update()
        check = input("Do you want to leave? ")
        if check == "yes":
            break

main()