#------------------------------------------------
# Lab 4 - Question 2 - Matteo Dagostino
#------------------------------------------------
'''2 – Write a program that receives a positive integer 𝑛 > 1. Then, it reads 𝑛 real numbers. Your
program should find the two numbers among these numbers that have the minimum difference. In
other words, find 𝑥 and 𝑦 in the array such that |𝑥 − 𝑦| is minimized. If there are more than one
pair with minimum difference, print the one that has smaller numbers. Check samples for
clarification.
Sample 1:
Input
    5
    56.17 61.15 14.56 13.21 29.92
Output
    13.21 14.56
Sample 2:
Input
    7
    19.98 20.01 20.02 18.96 20.20 20.21
Output
    20.01 20.02'''

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