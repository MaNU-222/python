import math

items = int(input("Enter the number of items: "))
per_box = int(input("Enter the number of items per box: "))

calc = math.ceil(items / per_box)
print()

print(f"For {items} items, packing {per_box} items in each box, you will need {calc} boxes")

