guess = "Malachi"
guess_count = 0

guess = input("What is the guess word? ")
while guess.lower() != "Malachi":
    print("You are not correct.")
    guess = input("What is your guess? ")
    guess_count = guess_count + 1
    if guess.lower() == "Malachi":
        print("Congratulations! YOu guessed it! ")
number_of_guesses = ""
print(f"It took you {guess_count} guesses. ")
print()
