#------------------------------------------------
# Assignment 1 - Question 4 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

n = int(input("Enter the amount of lines of Pascal's triangle you want to print: ")) #Asks for number

#---------------- Function for finding factorial ------------------------
def factorial(n): # Factorial function
    ans = 1 #The factorial answer  
    for i in range(1, n+1): #Loop from 1 to 1+(the number we want factorial)
        ans = ans * i # Answer = itself times i
    return ans #return the answer of the factorial to the place where the function was called

#---------------- Main loop for printing the Pascal triangle ------------------------
for i in range(0, n): #Loop until n amount of lines asked
    for j in range(0,n-i): # Find out how many spaces to print so that it looks like a pretty triangle
        print(" ", end = "") #Print out the spaces 
    for j in range(0, i+1): #Loop for how many numbers in that line
        print(" " + str(factorial(i) // (factorial(i - j) * factorial(j))), end = "") #Print the answer to that line individually
    print()# Print nothing (goes to next line)