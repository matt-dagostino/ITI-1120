#------------------------------------------------
# Lab 5 - Question 3 - Matteo Dagostino
#------------------------------------------------

import os
from pickle import FALSE #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

string1 = str(input("Input the first string: "))
string2 = str(input("Input the second string: "))

substring = False
if string2 > string1:
    for i in range(len(string2)-1, 0-1, -1):
        if string2[i] == string1[0]:
            substring = True
            for j in range(0, len(string1)):
                #print(j, "|", string2[i+j], "|", string1[j])
                if string2[i+j] != string1[j]:
                    substring = False
                    print("yes")
                    break
                if substring == True:
                    print()
                    print(string1 + " is a substring in " + string2)                    
                    print("The last occurence of " + string1 + " is at index", i)
                    print()
                    exit()


print()
if substring == False:
    print(string1 + " is not a substring in " + string2)
    print("The length of the second string is " + str(len(string2))) 
print()