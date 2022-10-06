#------------------------------------------------
# Assignment 1 - Question 9 - Matteo Dagostino
#------------------------------------------------

import os
import string #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

string1 = str(input("Enter the first string: ")) #Asks user for first string
string2 = str(input("Enter the second string: ")) #Asks user for second string


answer = [] #Create empty list for answer
for i in range(len(string2)): #Loop for the length of the second string
    if string2.startswith(string1, i): #If the second string starts with the first string, then,
        answer.append(i) #Add i (index) to answer list

if answer == []: #If the answer list is blank, then,
    print() #Print empty line 
    print("Error: \"" + string1 + "\" cannot be found in \"" + string2 + "\"") #Print error that the first string cannot be found in the second string
    print() #Print empty line 
    quit() # End program

string1reversed = string1[::-1] #Reverse the first string

real_Value = [] #List of actual values (negative), this helps to sort the numbers at the end
for i in range(len(string2)): #Loop for length of second string
    if string2.startswith(string1reversed, i): #If the second string starts with the first string(reversed), then,
        answer.append(((i+len(string1reversed)-1)*0.988965)) #Add i (index) + length of string reversed -1 * 0.988965 to answer list (multiplied so that it can sort my list easier (negative before positive)(placeholder))
        real_Value.append((i+len(string1reversed)-1)*-1) #Add the actual answer value to the real value list

answer = sorted(answer) #Sort the answer list

for i in range(0,len(real_Value)): #Loop for length of real value list
    for j in range(0,len(answer)): #Loop for length of actual answers
        if real_Value[i]*-1 == answer[j]/0.988965: #If the real value is found in a placeholder in the answers list, then,
            answer[j] = real_Value[i] #Replace the placeholder with the ACTUAL value

print("\nThe indexes where \"" + string1 + "\" can be found in \"" + string2 + "\" is at: ", end = "") #Print message before answers
print(*answer, sep = ", ") #Print answers (separated with comma)
print() #Print empty line 