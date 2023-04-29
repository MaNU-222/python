
print("AREA CALCULATOR")
print("SHAPES TO CALCULATE")
print("CIRCLE, SQUARE, RECTANCLE AND MORE.")
print()

import math

def compute_area_squre(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

shape = " "

while shape != "quit":
    shape = input("What shape do you have? ")

    shape = shape.lower()


    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = compute_area_squre(side)
        print(f"The area {area}")
        print(f"Your answer {area}")

    if shape == "circle":
        radius = float(("Waht is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area is {area}")
        print(f"Your answer {area}")

    if shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area_rectangle(length, width)
        print(f"The area is {area}")
        print(f"Your answer {area}")