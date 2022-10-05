#------------------------------------------------
# Lab 4 - Question 2 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

n = int(input("Enter a positive integer that is greater to 1: "))
list = []

for i in range(0,n):
    number = float(input( str(i+1) + ") Enter a number: "))
    list.append(number)

sorted_list = sorted(list)
answer =[]

smallest_gap = 10000 ** 100
for i in range(0, n-1):
    if sorted_list[i+1] - sorted_list[i] < smallest_gap:
        smallest_gap = sorted_list[i+1] - sorted_list[i]
        answer.append(sorted_list[i])
        answer.append(sorted_list[i+1])
        
print("-----------------------------------------------------------------------------------")
print("The minimum difference is between the two following numbers: " + str(answer[len(answer)-2]) + " and " + str(answer[len(answer)-1]))
print()