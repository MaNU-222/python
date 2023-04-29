import math

print("Tire Volume")
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect of ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000

print(f"The approximate tire volume is {volume:.2f} liters ")