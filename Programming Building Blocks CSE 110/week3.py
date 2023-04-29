print("MEAL PRICE CALCULATOR")
print("-"*22)

# THIS ASK USERS INPUT FOR THE FOLLOWING QUESTIONS
child = input("What is the price of a child's meal? $")
adult = input("What is the price of an adult's meal? $")
children = input("How many children are there? ")
adults = input("How many adults are there? ")
tax = input("What is the sales tax rate? ")
print()

#THIS CALCULATE THE PRICE OF CHILD MEAL TIMES NUMBER OF CHILDREN
price_child = float(child) * int(children)

#THIS CALCULATE THE PRICE OF ADULT MEAL TIMES NUMBER OF ADULTS
price_adult = float(adult) * int(adults)

#THIS ADD THE TWO PRICES TOGETHER
Subtotal = price_child + price_adult


#THIS PRINTS THE ABOVE STATEMENTS
#print("="*15)
print(f"Subtotal: ${float(Subtotal)}")
#print("="*15)