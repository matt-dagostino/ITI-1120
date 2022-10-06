#------------------------------------------------
# Lab 4 - Question 3 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
from collections import Counter # Imports the counter function which counts 

string1 = str(input("Enter the first string: "))
string2 = str(input("Enter the second string: "))

string1_count = Counter(string1) # Counts how many times the numbers are repeated in a list
string1_dict = string1_count.items() # Turns counter into a dictionary with (numberEntered, repeatedTimes)
string1_sorted = sorted(string1_dict)

string2_count = Counter(string2) # Counts how many times the numbers are repeated in a list
string2_dict = string2_count.items() # Turns counter into a dictionary with (numberEntered, repeatedTimes)
string2_sorted = sorted(string2_dict)

#print("String 1: " + str(string1_sorted))
#print("String 2: " + str(string2_sorted))

print("-------------------------------------")
if string1_sorted == string2_sorted:
    print("These strings are anagrams.")
else:
    print("These strings are not anagrams.")
print()