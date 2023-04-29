name = input("Please Enter your full name? ")
print(f"{name.title()}, Welcome to the game of Choice.")
print()
print("You are travelling around the world.")
choice = input("Do you want to use a (PLAIN) or a (CAR)? ")
if choice.lower() == "plain":
    print("You have to sit in the plain for 8 hours before you land for rest.")
    if choice.lower() == "plain":
        print()

choice = input("You have to stop in 8 hours to (TAKE) a nap or (BUILD) a shelter or (SEARCH) for water and fuel? ")
if choice.lower() == "take":
    print("Take a nap for 30 mins")
    print("Will  continue.")
elif choice.lower() == "build":
    choice = input("Go and (BUY) canopy or (SEARCH) for woods? ")
else:
    choice = input("Going for (WATER) or (FUEL) for the car? ")

if choice.lower() == "buy":
    print("The shop is two miles away")
    choice = input("will you go and come (YES) or (NO)? ")
if choice.lower() == "seach":
    print("fuel and water is about 2 miles.")
    choice = input("Will you use (CASH) or (CARD)? ")
        
if choice.lower() == "water":
    print("You will get some in the stream.")
    choice = input("Will you go to the (STREAM) or (QUIT)? ")
if choice.lower() == "fuel":
    print("There is no fuel around please return home.")
    choice = input("Do you want to find your way back home (YES) or (NO)?")

if choice.lower() == "yes":
    print("I will be back in 2 hours.")
    print("thank you")
if choice.lower() == "no":
    print("we will continue another day")
    print("Thank you")

if choice.lower() == "cash":
    print("You left your money at the appartmen.")
    choice = input("Will you go for it (MAYBE) or (MAYBE NOT)? ")
if choice.lower() == "card":
    print("insufficient Balance")
    choice = input("That means i have to return back to appartment (INDEED) or (NOT YET)? ")

if choice.lower  == "stream":
    print("it will take you an hour to reach the stream.")
    choice == input("will you go to the stream (Y) or (N)? ")
if choice.lower() == "quit":
    print(f"Thanks {name.title()} the journey was not easy.")

if choice.lower() == "yes":
    print(f"Thanks {name.title()} the journey was not easy.")
if choice.lower() == "no":
    print("so whats next.")
    print("you are out of options.")

if choice.lower() == "maybe":
    print("Game Over")
if choice.lower() == "maybe not":
    print("You are stack.")
    print("Game Over")
    
if choice.lower() == "indeed":
    print("End here.")
if choice.lower() == "not yet":
    print("out of options.")
    print("Game over.")

if choice.lower() == "y":
    print("Lets go to  the stream")
    choice = input("The stream has become a habitat for wild animal, will you (GO) or (RETURN)? ")
if choice.lower == "n":
    print("You are out of options")
    print("Game over.")

if choice.lower() == "go":
    print("You were eaten by Shark")
    print("Game Over.")
if choice.lower() == "return":
    print("You die with teste.")
    print("End Of Game")