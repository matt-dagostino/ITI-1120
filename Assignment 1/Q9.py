#------------------------------------------------
# Assignment 1 - Question 9 - Matteo Dagostino
#------------------------------------------------

import os
import string #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
'''
string1 = str(input("Enter the first string: "))
string2 = str(input("Enter the second string: "))
'''


string1 = "abdc"
string2 = "nbpabcggaccbaxu"

string1_array = []
for letter in string1:
    string1_array.append(letter)

string2_array = []
for letter in string2:
    string2_array.append(letter)

print(string1_array)
print(string2_array)

print(n for n in range(len(string2)) if string2.find(string1, n) == n)