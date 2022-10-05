#------------------------------------------------
# Assignment 1 - Question 6 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

'''
n = int(input("Enter the amount of numbers would you like to input: ")) #Asks for number (n)
numbers =[]

for i in range(0,n):
    num = (float(input(str(i+1) + ") Enter a number: ")))
    numbers.append(num)
'''
n=10
numbers =[82.34, 81.71,76.25, 76.25, 68.72, 61.21, 95.67, 70.58, 61.21, 55.74]
#---------------------------- Calculate Average ------------------------------
ans = 0
for i in range(0,n):
    ans = ans + numbers[i]
ans = ans / n
print("Average:",ans)

#---------------------------- Calculate Mode ------------------------------
from statistics import multimode
mode = multimode(numbers)
mode = sorted(mode)
print("Mode: ", end = "")
print(*mode, sep=", ")

#---------------------------- Calculate Median ------------------------------
sorted_list = sorted(numbers)
middle = n // 2
median = (sorted_list[middle] + sorted_list[middle-1])/2
print("Median: " + format(median, '.3f'))
