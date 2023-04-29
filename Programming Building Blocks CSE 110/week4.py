print("-"*16)
print("MEAL CALCUALTTOR")
print("-"*16)

child = input("What is the price of a child's meal? $")
adult = input("What is the price of an adult's meal? $")
children = input("How many children are there? ")
adults = input("How many adults are there? ")
tax = input("What is the sales tax rate(%)? ")
print()

price_child = float(child) * int(children)
price_adult = float(adult) * int(adults)
Subtotal = price_child + price_adult
print(f"Subtotal: ${float(Subtotal):.2f}") 

sales_tax = Subtotal * float(tax) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

print()
total = Subtotal + sales_tax
print(f"Total: ${float(total):.2f}")

print("="*55)   # this allows the equal sign to multiply it self and bcome a format.
print("If you received great service, please consider tipping:")
print(" 10% = $1 ")
print(" 15% = $1 ")
print(" 20% = $2 ")
print(" 30% = $2 ")
print(" 50% = $3 ")
print(" 70% = $3.50")
print(" 80% = $4 ")
print(" 99% = $5 ")
print(" 99% = $5 ")
print("="*55)

tip = input("How many dollars do you want to leave? $")
tip_plus = float(total) + float(tip)

print("."*23)
print(f"Total plus tip: ${tip_plus:.2f}")
amount = input("Amount Paid? $")
change = float(amount) - float(tip_plus)
print(f"Change dua: ${change:.2f}")
print("."*23)