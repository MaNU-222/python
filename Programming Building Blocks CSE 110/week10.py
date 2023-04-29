quantities = []
item_list = []
item_prices = []
number = 0
total = 0

while number != "6":
    print("welcome to the shopping cart.")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove")
    print("4. Compute Total")
    print("5. Quit")
    action = input("Please Enter an action: ")
    
    if action == "1":
        item_name = input ("What item would you like to add? ")
        quantity = int(input("Enter Quantity: "))
        item_price = float(input(f"What is the price of'{item_name}'?$ "))
        # how can i multiply quantity by item_price to show it in the total.
         

        item_list.append(item_name)
        item_prices.append(item_price)
        quantities.append(quantity)
	    
        print(f"{item_name.title()} has been added to cart.") 
    
    elif action == "2":
        print()
        print("The Content Of The Shopping Cart Are:") 
        print("ITEM - QUANTITY - PRICE")   
        for i in range(len(item_list)):
	        print(f"{i + 1 }.{item_list[i].title()} - {quantities[i]} - ${item_prices[i]:.2f}")

    elif action == "3":
        remove_item = int(input("What item index would you like to remove? "))
        item_prices.pop(remove_item - 1)
        item_list.pop(remove_item - 1)
        quantities.pop(remove_item - 1)
        print("ITEM REMOVED!!!.")
           


    elif action == "4":
        for price in item_prices:
	        total += item_price  
        print()
        print("The total price of the item in the shopping cart are:")
        print(f"Total: ${total:.2f}")


    else:
        print("THE ACTION YOU ENTERED IS NOT VALID!!")
        print()