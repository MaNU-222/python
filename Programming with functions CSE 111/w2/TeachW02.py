# we import the datetime module so that it can be used in this program.
from datetime import datetime

#the discount rate is 10% and thw sales tax rate is 6%
Disc_rate = 0.01
sales_tax_rate = 0.06

# get the subtotal from the user
subtotal = float(input("Please enter the subtotal: "))

# call the now method to get the current date and time
# as the datetime object from the computer operating system
current_date_and_time = datetime.now()

# call the week day method to get the day of the week from current date time object 
weekday = current_date_and_time.weekday()


if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * Disc_rate, 2)
    print(f"Discount Amount: {discount:.2f}")
    subtotal -= discount


sales_tax = round(subtotal * sales_tax_rate, 2)
print(f"Sales Tax Amount: {sales_tax:.2f} ")

total = subtotal + sales_tax

print(f"Total: {total:.2f} ")