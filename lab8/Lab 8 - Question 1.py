#------------------------------------------------
# Lab 7 - Question 1 - Matteo Dagostino
#------------------------------------------------

import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

universal = set()
A = set()
B = set()

def get_sets(message):
    temp = set()
    x = int(input("Enter the amount of numbers that would you like to add to the " + message + " set: "))
    for i in range(0,x):
        temp.add(int(input(str(i+1) + ") Enter a number to add: ")))
    return temp

universal = get_sets("universal")
A = get_sets("A")
B = get_sets("B")

print("------------------------------------------------------------")
print("A union B: " + str(sorted(A.union(B))))
print("A intersection B: " + str(sorted(A.intersection(B))))
print("A - B: " + str(sorted(A.difference(B))))
print("B - A: " + str(sorted(B.difference(A))))
print("A Complement: " + str(sorted(universal.difference(A))))
print("B Complement: " + str(sorted(universal.difference(B))))
print("A ^ B: " + str(sorted(universal.difference(A).difference((universal.difference(B))).union((universal.difference(B)).difference((universal.difference(A)))))))
if A.issubset(B):
    if B.issubset(A):
        print("A is a subset of B, and B is a subset of A")
    else:
        print("A is a subset of B, and B is not a subset of A")
else:
    if B.issubset(A):
        print("A is not a subset of B, and B is a subset of A")
    else:
        print("A is not a subset of B, and B is not a subset of A")
print("------------------------------------------------------------")
