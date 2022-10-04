#------------------------------------------------
# Assignment 1 - Question 5 - Matteo Dagostino
#------------------------------------------------

from platform import java_ver
import random
import os
from re import T #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

n = int(input("Enter a non-negative integer: ")) #Asks for number (n)
p = int(input("Enter the amount of players: ")) #Asks for number (player)
scores = {
    }
list_score = []
list_name = []

for p in range(1,p+1):
    print()
    name = str(input("Please enter the name of player " + str(p) + ": "))
    score = 0
    correct = False
    x = random.randint(0, n)
    
    while correct == False:
        guess = int(input("Enter your guess: "))
        if guess > x:
            print("Your guess is too big!")
            score += 1
        elif guess < x:
            print("Your guess is too small!")
            score += 1
        elif guess == x:
            score += 1
            print("You guessed it right with " + str(score) + " guesses!")
            scores[p] = str(score), str(name)
            list_name.append(name)
            list_score.append(score)
            correct = True

winner = ""
print("------------------ Results ------------------ ")
print("{:<13} {:<10} {:<9}".format('Player','Name','Amount of guesses'))
for player, value in scores.items():
    guesses, name = value
    print("{:<13} {:<10} {:<9}".format(player, name, guesses))


print("------------------ Winner(s) ------------------ ")
newlist= []
small = 100
for i in range(0, len(list_score)):
    if small >= list_score[i]:
        newlist.append(i)
        for j in range(0, len(list_score)):
            if list_score[i] > list_score[j]:
                newlist.remove(i)
                break

for i in range(0, len(newlist)):
        print("--> " + str(list_name[newlist[i]]))

print()