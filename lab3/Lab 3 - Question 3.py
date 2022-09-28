import os
import random

again = "yes"

while again == "y" or again == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')
    n = int(input("\033[1;37mEnter a non-negative integer:\033[0;34m "))
    randomNumber = random.randint(0,n+1)
    print("\033[1;36mA random number has been generated!")

    while 1 > 0:
        guess = int(input("\033[1;37mEnter your guess:\033[0;34m  "))
        if guess > randomNumber:
            print("\033[0;31mYour guess is too large!")
        elif guess < randomNumber:
            print("\033[0;31mYour guess is too small!")
        else:
            print("\033[0;32mYou guessed it right!")
            again = str(input("\033[1;31mWould you like to play again? (Y/N):\033[0;34m "))
            again = str.lower(again)
            break

print("\033[1m\033[0;32mThanks for playing!\n")