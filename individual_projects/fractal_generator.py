# BHR 2nd fractal generator
from helper import *
import turtle as t

#Create a main loop
def main():
    while True:
        t.clearscreen()
        quantity = int_input([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "What do you want the recursion depth to be? (1-5). ")
        color = choice_input(["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white", "bisque"], "What do you want the color of the triangles to be? ")
        #t.tracer(0, 0)
        t.color(color)
        t.teleport((-250/2**((quantity-5)*-1)), (-250/2**((quantity-5)*-1)))
        generator(quantity)
        #t.update()
        check = input("Do you want to leave? ")
        if check == "yes":
            break

# create the recursive function
def generator(quantity):
    if quantity == 1:
        for i in range(3):
            t.forward(500 / (2**((quantity-5)*-1)))
            t.left(120)
        return 1
    for i in range(3):
        for i in range(3):
            t.forward(500 / (2**((quantity-5)*-1)))
            t.left(120)
        generator(quantity -1)
        t.forward(500 / (2**((quantity-5)*-1)))
        t.left(120)

main()