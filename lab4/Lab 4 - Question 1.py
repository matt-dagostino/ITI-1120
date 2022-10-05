#------------------------------------------------
# Lab 4 - Question 1 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
from collections import Counter # Imports the counter function which counts 

n = int(input("Enter a positive integer that is greater to 2: "))
list = []

for i in range(0,n):
    number = int(input( str(i+1) + ") Enter a number: "))
    list.append(number)

c = Counter(list) # Counts how many times the numbers are repeated in a list
final_list = c.items() # Turns counter into a dictionary with (factorNumber, repeatedTimes)
answer = []
small = 10000
for numberEntered, repeatedTimes in final_list:
    if repeatedTimes <= small:
        small = repeatedTimes
        answer.append(numberEntered)
        for numberEntered2, repeatedTimes2 in final_list:
            if repeatedTimes > repeatedTimes2:
                answer.pop()
                break
print("----------------------------------------")
print ("The unique number: ", end = "")
print(*answer, sep = ", ")
print()