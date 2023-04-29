
print()
print("Welcome to the HINT Game!")

secret_word = "mosiah"

mask = ""

for i in secret_word:
    mask = mask + "_ "
print(f"Your hint is: {mask}")

guess = input("What is your guess? ")
guess = guess.lower()
count = 1
while (secret_word != guess):

    letter = "_"

    mask = ""

    for i, a in enumerate (guess):
        letter = "_"

        for j, b in enumerate (secret_word):

            if (a == b and i == j):
                letter = a.capitalize() + ""
            elif (a == b):
                letter = a + ""
        mask = mask + letter
    print(f"Your hint is {mask}") 

    print("Wrong, try again")
    guess = input("What is your guess? ")
    guess = guess.lower()
    count += 1
print("Congratulations you guessed it right")
print(f"It took you {count} number of guesses")
print()