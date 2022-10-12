#------------------------------------------------
# Assignment 1 - Question 3 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console


#---------------- Inputs and set variables ------------------------
x = float(input("Enter the x value: ")) #Asks for x value
n = int(input("Enter the n value: ")) #Asks for n value
cosx = float(1) #Sets predetermined value for cosx
sinx = float(x) #Sets predetermined value for sinx

#---------------- Function for finding factorial ------------------------
def factorial(n): # Factorial function
    ans = 1 #The factorial answer  
    for i in range(1, n+1): #Loop from 1 to 1+(the number we want factorial)
        ans = ans * i # Answer = itself times i
    return ans #return the answer of the factorial to the place where the function was called

#---------------- Finding cosx ------------------------
j=2 #Preset value of j
for i in range(2,1+2*(n-1), 2): #Loop to find out the denominator numbers (and powers)
    if j % 2 == 0: #Simple if function to see if we should start with - or + for next term
        cosx = cosx - ((x ** i)/factorial(i)) #Get answer of cosx
    else: #Simple if function to see if we should start with - or + for next term
        cosx = cosx + ((x ** i)/factorial(i)) #Get answer of cosx
    j +=1 # Add 1 to j

#---------------- Finding sinx ------------------------
j=2 #Preset value of j
for i in range(3,1+2*(n), 2): #Loop to find out the denominator numbers (and powers)
    if j % 2 == 0: #Simple if function to see if we should start with - or + for next term
        sinx = sinx - ((x ** i)/factorial(i)) #Get answer of sinx
    else: #Simple if function to see if we should start with - or + for next term
        sinx = sinx + ((x ** i)/factorial(i)) #Get answer of sinx
    j +=1 # Add 1 to j

#---------------- Printing answers ------------------------
print("Sin(" + str(x) + ") = " + format(sinx, '.7f')) #Print sinx
print("Cos(" + str(x) + ") = " + format(cosx, '.7f')) #Print cosx
