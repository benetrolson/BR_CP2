# BHR 2nd fractal generator
from helper import *
import turtle as t

#Create a main loop
def main():
    while True:
        t.clearscreen()
        quantity = int_input([1, 2, 3, 4, 5], "What do you want the recursion depth to be? (1-5). ")
        color = choice_input(["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white", "bisque"], "What do you want the color of the triangles to be? ")
        background_color = choice_input(["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white", "bisque"], "What do you want the color of the background to be? ")
        fractal = choice_input(["sierpinski", "sierpinski triangle", "koch", "koch snowflake"], "What fractal do you want to make? ")
        t.tracer(0, 0)
        t.color(color)
        t.bgcolor(background_color)
        t.teleport((-250/2**((quantity-5)*-1)), (-250/2**((quantity-5)*-1)))
        if fractal in["sierpinski", "sierpinski triangle"]:
            sierpinski(quantity)
        elif fractal in ["koch", "koch snowflake"]:
            koch(400, quantity)
        t.update()
        check = input("Do you want to leave? ")
        if check == "yes":
            break

# create the recursive function
def sierpinski(quantity):
    if quantity == 1:
        for i in range(3):
            t.forward(500 / (2**((quantity-5)*-1)))
            t.left(120)
        return 1
    for i in range(3):
        for _ in range(3):
            t.forward(500 / (2**((quantity-5)*-1)))
            t.left(120)
        sierpinski(quantity -1)
        t.forward(500 / (2**((quantity-5)*-1)))
        t.left(120)

def koch(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch(length/3, depth-1)
        t.left(60)
        koch(length/3, depth-1)
        t.right(120)
        koch(length/3, depth-1)
        t.left(60)
        koch(length/3, depth-1)

main()
