#------------------------------------------------
# Assignment 1 - Question 10 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

row = int(input("Enter the number of rows: ")) #Asks for rows
column = int(input("Enter the number of columns: ")) #Asks for columns

squares = 0 #Set number of squares to 0
for i in range(0,row): #Loop from 0 to however many rows
    squares = squares + (row-i)*(column-i) #Count the amount of squares

print("-------------- Answers --------------") #Print title for answers
print("Total number of rectangles = " + str(int(row*(row+1)*column*(column+1)/4))) #Print total number of rectangles
print("Rectangles but not squares = " + str(int((row*(row+1)*column*(column+1)/4)) - squares)) #Print total number of rectangles - amount of squares to give us rectangles but not squares
print() #Print empty line