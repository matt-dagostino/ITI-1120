#------------------------------------------------
# Midterm 1 - Question 1 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

prime_list= [] # Create list where prime numbers will be stored
x = int(input("Enter a number bigger than 2: ")) # Ask for user to input number

for i in range(2, x): # Loop from 2 to the number that the user entered
    prime = True # Set prime to True
    for j in range(2, i): #Loop from 2 to i
        if i % j == 0 and i != j: # If the number is divisable and not equal to itself, then
            prime = False # Prime is set to False
            break #End loop (line 14)
    if prime == True: #If prime is True
        prime_list.append(i) #Add i (the prime number) to the list of prime numbers

for i in range (0, len(prime_list)): #Loop from 0 to the length of prime numbers
    for j in range (0, len(prime_list)): #Loop from 0 to the length of prime numbers
        if prime_list[i] + prime_list[j] == x: #Check if two numbers added together equals the number the user entered, if yes, then
            print("-------------------------------------- Output --------------------------------------") #Print divider
            print(str(x) + ' = ' + str(prime_list[i]) + " + " + str(prime_list[j])) #Print output
            print() #Print empty line (make the program look better)
            exit() #Exit program

# If you wanted to see all possibilities, remove line 25
