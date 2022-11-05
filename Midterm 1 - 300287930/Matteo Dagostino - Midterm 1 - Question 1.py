#------------------------------------------------
# Midterm 1 - Question 1 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

prime_list= []
x = int(input("Enter a number bigger than 2: "))

for i in range(2, x):
    prime = True
    for j in range(2, i):
        if i % j == 0 and i != j:
            prime = False
            break
    if prime == True:
        prime_list.append(i)

for i in range (0, len(prime_list)):
    for j in range (0, len(prime_list)):
        if prime_list[i] + prime_list[j] == x:
            print(str(x) + ' = ' + str(prime_list[i]) + " + " + str(prime_list[j]))
            print()
            exit()
