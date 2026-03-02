# BHR 2nd fractal generator
from helper import *
import turtle as t

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

