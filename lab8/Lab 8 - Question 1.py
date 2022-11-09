#------------------------------------------------
# Lab 8 - Question 2 - Matteo Dagostino
#------------------------------------------------

import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

""" A = [[12, 22, 33, 56, 11], 
    [15, 10, 21, 9, 18],
    [0,  0, 0, 0, 8],
    [7,  0, 0, 0, 0],
    [10, 1,2,3,6]]

n = 4
 """

A = []
n = int(input("Enter the dimensions of the matrix (L x L): "))
for i in range(0,n):
    string = str(input(str(i+1) + ") Enter the line: "))
    string = string.split()
    A.append(string)

""" 
i = 0
[i][n-1]
[i][n-2]
[i][n-3]
i++ (1)
[i][n-1]
[i][n-2]
i++(2)
[i][n-1]
 """
lower = True
for i in range(0,n-1): #0,1,2,3
    for j in range(1,n-i): #1,2,3 -> #1,2 -> #1
        if A[i][n-j] != "0":
            lower = False
            break


""" 
i = 0
[i][n-1]
[i][n-2]
[i][n-3]
i++ (1)
[i][n-1]
[i][n-2]
i++(2)
[i][n-1]
 """
upper = True
for i in range(0,n-1): #0,1,2,3
    for j in range(1,n-i): #1,2,3 -> #1,2 -> #1
        if A[n-j][i] != "0":
            upper = False
            break



print("------------------------ Output ------------------------")
print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in A]))
print()

if lower == False and upper == False:
    print("This matrix is neither upper nor lower triangular.")
elif lower == True and upper == True:
    print("This matrix is both lower and upper triangular.")
elif lower == True:
    print("This matrix is lower triangular.")
elif upper == True:
    print("This matrix is upper triangular.")
print()
