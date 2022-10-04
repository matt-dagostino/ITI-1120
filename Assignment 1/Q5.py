#------------------------------------------------
# Assignment 1 - Question 5 - Matteo Dagostino
#------------------------------------------------

from platform import java_ver
import random
import os
from re import T #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

#---------------- Initiation of variables and inputs ------------------------
n = int(input("Enter a non-negative integer: ")) #Asks for number (n)
p = int(input("Enter the amount of players: ")) #Asks for number (player)
scores = { #Create dictionary for end results
    }
list_score = [] # Create list for scores
list_name = [] # Create list of names

for p in range(1,p+1): #Do while x amount of players
    print() #Print empty line
    name = str(input("Please enter the name of player " + str(p) + ": ")) #Ask for the player's name
    score = 0 #Set score to 0
    correct = False #Did the player guess the answer? Preset = False
    x = random.randint(0, n) #Create random number from 0 to n (inclusive)
    
    while correct == False: #While the player didnt get the answer, then,
        guess = int(input("Enter your guess: ")) #Ask for guess
        if guess > x: #If guess is too big
            print("Your guess is too big!") #Print hint
            score += 1 #Add 1 to player's score
        elif guess < x: #If guess is too small
            print("Your guess is too small!") #Print hint
            score += 1 #Add 1 to player's score
        elif guess == x: #If player got the answer right
            score += 1 #Add 1 to player's score
            print("You guessed it right with " + str(score) + " guesses!") #Print how many guesses it took to get right
            scores[p] = str(score), str(name) #Add info to dictionary
            list_name.append(name) #Add name to name list  
            list_score.append(score) #Add score to score list
            correct = True #Player got the answer = True

print("------------------ Results ------------------ ") #Print divider
print("{:<13} {:<10} {:<9}".format('Player','Name','Amount of guesses')) #Using formatting, print the title of the results table
for player, info in scores.items(): #Get info from dictionary
    guesses, name = info #Add values to guesses and name
    print("{:<13} {:<10} {:<9}".format(player, name, guesses)) #Print player, name and guesses taken


print("------------------ Winner(s) ------------------ ") #Print divider
newlist= [] #Create list
small = 100 #Store 100 in variable
for i in range(0, len(list_score)): #Loop from 0 to length of score (times played)
    if small >= list_score[i]: #If the score is smaller than previous score then,
        newlist.append(i) #Add index of smallest number to list (newlist)
        for j in range(0, len(list_score)): #Loop from 0 to length of score (times played)
            if list_score[i] > list_score[j]: #If there is a smaller guess in the list, then,
                newlist.remove(i) #Remove last added index in list
                break #Stop loop since we already found what we wanted from this loop

for i in range(0, len(newlist)): #Loop from 0 to length winners
        print("--> " + str(list_name[newlist[i]])) #Print winner(s)

print()#Print empty line