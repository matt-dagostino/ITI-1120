import os
import random

again = "yes"

while again == "y" or again == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')
    n = int(input("Enter a non-negative integer: "))
    randomNumber = random.randint(0,n+1)
    print("A random number has been generated!")

    while 1 > 0:
        guess = int(input("Enter your guess:  "))
        if guess > randomNumber:
            print("Your guess is too large!")
        elif guess < randomNumber:
            print("Your guess is too small!")
        else:
            print("You guessed it right!")
            again = str(input("Would you like to play again? (Y/N): "))
            again = str.lower(again)
            break

print("Thanks for playing!\n")