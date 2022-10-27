#------------------------------------------------------------
# Assignment 2 - Master Mind - Matteo Dagostino (300287930)
#------------------------------------------------------------
import os #Import os for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
import random #Important random
answer_colors= [] # Make a list for the answers
red, yellow, blue, green, orange, pink, purple, cyan, silver, teal = False, False, False, False, False, False, False, False, False, False # Set false so that colors don't get repeated
colors = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "cyan", "silver", "teal"] # List of available colors
penalties = 0 # Sets the user's penalties to 0

while len(answer_colors) != 4: # Do until there are 4 colors picked
    x = random.randint(1,10) #Chose a random number between 1 and 10 (included)
    if x == 1: # If the random number is 1, then
        if red == False: # If this color isn't already in the list of chosen colors, then
            red = True # Set this color as chosen color
            answer_colors.append('red') # Add the color to the list of chosen colors
    elif x == 2: # If the random number is 2, then
        if yellow == False: # If this color isn't already in the list of chosen colors, then
            yellow = True # Set this color as chosen color
            answer_colors.append('yellow') # Add the color to the list of chosen colors
    elif x == 3: # If the random number is 3, then
        if blue == False: # If this color isn't already in the list of chosen colors, then
            blue = True # Set this color as chosen color
            answer_colors.append('blue') # Add the color to the list of chosen colors
    elif x == 4: # If the random number is 4, then
        if green == False: # If this color isn't already in the list of chosen colors, then
            green = True # Set this color as chosen color
            answer_colors.append('green') # Add the color to the list of chosen colors
    elif x == 5: # If the random number is 5, then
        if orange == False: # If this color isn't already in the list of chosen colors, then
            orange = True # Set this color as chosen color
            answer_colors.append('orange') # Add the color to the list of chosen colors
    elif x == 6: # If the random number is 6, then
        if pink == False: # If this color isn't already in the list of chosen colors, then
            pink = True # Set this color as chosen color
            answer_colors.append('pink') # Add the color to the list of chosen colors
    elif x == 7: # If the random number is 7, then
        if purple == False: # If this color isn't already in the list of chosen colors, then
            purple = True # Set this color as chosen color
            answer_colors.append('purple') # Add the color to the list of chosen colors
    elif x == 8: # If the random number is 8, then
        if cyan == False: # If this color isn't already in the list of chosen colors, then
            cyan = True # Set this color as chosen color
            answer_colors.append('cyan') # Add the color to the list of chosen colors
    elif x == 9: # If the random number is 9, then
        if silver == False: # If this color isn't already in the list of chosen colors, then
            silver = True # Set this color as chosen color
            answer_colors.append('silver') # Add the color to the list of chosen colors
    elif x == 10: # If the random number is 10, then
        if teal == False: # If this color isn't already in the list of chosen colors, then
            teal = True # Set this color as chosen color
            answer_colors.append('teal') # Add the color to the list of chosen colors

name = str(input("Enter your name: ")) # Ask the user for their name
print("--------------------------------------------------------------------------------------------") # Divider line
print("Welcome to Master Mind " + name + "!") # Print instructions for user
print("The code maker is here. Available colors are:") # Print instructions for user
print("Red, Yellow, Blue, Green, Orange, Pink, Purple, Cyan, Silver, Teal") # Print instructions for user
print("You have 15 guesses, total of 5 penalties are allowed but avoid penalties.") # Print instructions for user
print("The code maker selected 4 colors.") # Print instructions for user
print("When entering guesses, enter each color followed by a space. (Example: Red Green Yellow Blue)") # Print instructions for user
print("You can start guessing " + name + ".") # Print instructions for user

tries = 0 # Set the amount of tries to 0
while tries != 15: #Do the following as long as the user hasn't reached 15 tries
    print("--------------------------------------------------------------------------------------------") # Divider line
    guess = input("Enter guess number " + str(tries+1) + ": ") # Ask the user for their guess
    guess = guess.lower() #Set the guess to all lower characters
    guess = guess.split() #Split the guess within parts (using " " as a seperator)
    if len(guess) == 4: # If the guess contains 4 colors, then
        valid = True # Set valid to true
        for j in range(0,4): #Loop from 0 to 4
            if guess[0] == guess[1] or guess[0] == guess[2] or guess[0] == guess[3] or guess[1] == guess[2] or guess[1] == guess[3] or guess[2] == guess[3]: # If the color is repeated, then
                print("Sorry " + name + ", repeated colors are not allowed in this game. One penalty is considered.") # Print error message
                penalties = penalties + 1 # Add a penalty
                print("Total penalties: " + str(penalties)) # Print the amount of penalties
                valid = False # Set valid to false
                tries = tries - 1 # Remove 1 try from the user
                break # End for loop
            if guess[j] not in colors:
                print("Sorry " + name + ", we cannot recognize the colors you entered. One penalty is considered.") # Print error message
                penalties = penalties + 1 # Add a penalty
                print("Total penalties: " + str(penalties)) # Print the amount of penalties
                valid = False # Set valid to false
                tries = tries - 1 # Remove 1 try from the user
                break # End for loop
        if valid == True: # If valid is true, then
                black = 0 # Set the user's black amount to 0
                white = 0 # Set the user's white amount to 0
                for j in range(0,4): # Loop from 0 to 4
                    if guess[j] in answer_colors: # If the 'j' (0,1,2,3) guess is in the answer colors then,
                        white = white + 1 # Add 1 white
                        if guess[j] == answer_colors[j]: # If the user guessed the proper position of the color, then
                            white = white - 1 # Remove 1 white (replace with black)
                            black = black + 1 # Add 1 black
                print("You got " + str(black) + " black, and " + str(white) + " white for this guess.") # Print to the user how many blacks and whites they got correct
                if black == 4: # If the user guessed correctly, then
                    print("Congratulations " + name + " you won the game with " + str(tries+1) + " guesses and " + str(penalties) + " penalties!") #Print congratulations message
                    print("--------------------------------------------------------------------------------------------") # Divider line
                    exit() # End program
    elif len(guess) != 4: # If the user didnt enter 4 colors, then
        print("Sorry " + name + ", you need to enter at least 4 colors for each guess. One penalty is considered.") # Print error message
        penalties = penalties + 1 # Add a penalty
        print("Total penalties: " + str(penalties)) # Print the amount of penalties
        tries = tries - 1 # Remove 1 try from the user
    if penalties == 5: # If the user has reached 5 penalties, then
        print(name + ", you lost the game by reaching the maximum number of allowed penalties.") # Print error message
        print("--------------------------------------------------------------------------------------------") # Divider line
        exit() # End program
    tries = tries +1 # Add 1 try to the amount of tries
    if tries == 15: # If the user used 15 tries
        print("Sorry " + name + ", you ran out of guesses and you lost the game with " + str(penalties) + " penalties.") # Print error message
        print("--------------------------------------------------------------------------------------------") # Divider line