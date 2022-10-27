#------------------------------------------------------------
# Assignment 2 - Master Mind - Matteo Dagostino (300287930)
#------------------------------------------------------------
import os #Import os for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
import random #Important random
answer_colors= [] # Make a list for the answers
red, yellow, blue, green, orange, pink, purple, cyan, silver, teal = False, False, False, False, False, False, False, False, False, False
colors = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "cyan", "silver", "teal"]
penalties = 0

while len(answer_colors) != 4:
    x = random.randint(1,10)
    if x == 1:
        if red == False:
            red = True
            answer_colors.append('red')
    elif x == 2:
        if yellow == False:
            yellow = True
            answer_colors.append('yellow')
    elif x == 3:
        if blue == False:
            blue = True
            answer_colors.append('blue')
    elif x == 4:
        if green == False:
            green = True
            answer_colors.append('green')
    elif x == 5:
        if orange == False:
            orange = True
            answer_colors.append('orange')
    elif x == 6:
        if pink == False:
            pink = True
            answer_colors.append('pink')
    elif x == 7:
        if purple == False:
            purple = True
            answer_colors.append('purple')
    elif x == 8:
        if cyan == False:
            cyan = True
            answer_colors.append('cyan')
    elif x == 9:
        if silver == False:
            silver = True
            answer_colors.append('silver')
    elif x == 10:
        if teal == False:
            teal = True
            answer_colors.append('teal')

print(answer_colors)

name = str(input("Enter your name: "))
print("--------------------------------------------------------------------------------------------")
print("Welcome to Master Mind " + name + "!")
print("The code maker is here. Available colors are:")
print("Red, Yellow, Blue, Green, Orange, Pink, Purple, Cyan, Silver, Teal")
print("You have 15 guesses, total of 5 penalties are allowed but avoid penalties.")
print("The code maker selected 4 colors.")
print("When entering guesses, enter each color followed by a space. (Example: Red Green Yellow Blue)")
print("You can start guessing " + name + ".")
tries = 0

while tries != 15:
    print("--------------------------------------------------------------------------------------------")
    guess = input("Enter guess number " + str(tries+1) + ": ")
    guess = guess.lower()
    guess = guess.split()
    if len(guess) == 4:
        valid = True
        for j in range(0,4):
            if guess[0] == guess[1] or guess[0] == guess[2] or guess[0] == guess[3] or guess[1] == guess[2] or guess[1] == guess[3] or guess[2] == guess[3]:
                print("Sorry " + name + ", repeated colors are not allowed in this game. One penalty is considered.")
                penalties = penalties + 1
                print("Total penalties: " + str(penalties))
                valid = False
                tries = tries - 1
                break
            if guess[j] not in colors:
                print("Sorry " + name + ", we cannot recognize the colors you entered. One penalty is considered.")
                penalties = penalties + 1
                print("Total penalties: " + str(penalties))
                valid = False
                tries = tries - 1
                break
        if valid == True:
                black = 0
                white = 0
                for j in range(0,4):
                    if guess[j] in answer_colors:
                        white = white + 1
                        if guess[j] == answer_colors[j]:
                            white = white - 1
                            black = black + 1
                print("You got " + str(black) + " black, and " + str(white) + " white for this guess.")
                if black == 4:
                    print("Congratulations " + name + " you won the game with " + str(tries+1) + " guesses and " + str(penalties) + " penalties!")
                    print("--------------------------------------------------------------------------------------------")
                    exit()
    elif len(guess) != 4:
        print("Sorry " + name + ", you need to enter at least 4 colors for each guess. One penalty is considered.")
        penalties = penalties + 1
        print("Total penalties: " + str(penalties))
        tries = tries - 1
    if penalties == 5:
        print(name + ", you lost the game by reaching the maximum number of allowed penalties.")
        print("--------------------------------------------------------------------------------------------")
        exit()
    tries = tries +1
    if tries == 15:
        print("Sorry " + name + ", you ran out of guesses and you lost the game with " + str(penalties) + " penalties.")
        print("--------------------------------------------------------------------------------------------")