#------------------------------------------------
# Lab 8 - Question 2 - Matteo Dagostino
#------------------------------------------------

import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

A = []
n = int(input("Enter the amount of rows: "))
for i in range(0,n):
    string = str(input(str(i+1) + ") Enter the line: "))
    A.append(string)

string = str(input("Enter the string to find: "))
guess = []
for char in string:
    guess.append(char)

B =[]
for word in A:
    x = len(word)
    C = []
    for char in word:
        C.append(char)
    B.append(C)

vertical = True
horizontal = True
diagonal = True

for i in range(0,n):
    for j in range(0,x):
        if string[0] == A[i][j]:
            vert = 0
            horizon = 0
            diag = 0
            for h in range(1,len(string)):
                vert = vert + 1
                if i > len(string):
                    break
                if i != n-1:
                    if A[i+h][j] != string[h]:
                        break
                if i == n-1:
                    break
                if vert == len(string)-1:
                    print("------------------------ Output ------------------------")
                    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in A]))
                    print("\n" + string + " is at row " + str(i+1) + " and column " + str(j+1) + " vertically.\n")
                    exit()
            #--------- HORIZONTAL ----------
            for h in range(1,len(string)):
                horizon = horizon + 1
                if x-len(string) < j:
                    break
                if A[i][j+h] != string[h]:
                    break
                if horizon == len(string)-1:
                    print("------------------------ Output ------------------------")
                    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in A]))
                    print("\n" + string + " is at row " + str(i+1) + " and column " + str(j+1) + " horizontally.\n")
                    exit()
            #--------- DIAGONALLY ----------
            for h in range(1,len(string)):
                diag = diag + 1
                if x-len(string) < j and i > len(string):
                    break
                if i != n-1:
                    if A[i+h][j+h] != string[h]:
                        break
                if i == n-1:
                    break
                if diag == len(string)-1:
                    print("------------------------ Output ------------------------")
                    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in A]))
                    print("\n" + string + " is at row " + str(i+1) + " and column " + str(j+1) + " diagonally.\n")
                    exit()
 
print("------------------------ Output ------------------------")
print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in A]))
print()