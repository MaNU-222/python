import math
from datetime import datetime

date = datetime.now()

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect of ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000

if width >= 195 and aspect_ratio >= 55 and diameter >= 15:
    price = 95.59

elif width > 195 and aspect_ratio > 50 and diameter > 14:
    price = 75.99

elif width > 175 and aspect_ratio > 40 and diameter > 13:
    price = 55.59

elif width <= 175 and aspect_ratio <= 40 and diameter <= 13:
    price = 45.99

print()
print(f"The price is ${price}")
print("=" * 19)

purchase = input("Please do you want to buy (yes/no): ")

if purchase.lower() == "yes":
    number = input("PLease Enter Your Telephone number: ")
    print()
    print(f"This is your contact: {number}")
    print("THANK YOU!!")

else:
    print("THANK YOU!! FOR YOUR TIME")
    quit()


with open("volume.txt", mode="at") as volumes:
    print(f"{date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, My contact is: ({number})",  file=volumes )
