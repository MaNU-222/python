item_list = []
number = 1

while number != "5":
    print("welcome to the shopping cart.")
    print("1. add item")
    print("2. view cart")
    print("3. remove")
    print("4. compute total")
    print("5. quit")
    action = input("please enter an action: ")
    
    if action == "1":
        item_name = input ("what item would you like to add? ")
        
        item_list.append(item_name)
        print(f"{item_name.title()} has been added to cart.") 
    
    if action == "2":
        print("the content of the shopping cart are:")
        
        for item in item_list:
            print(item)
      