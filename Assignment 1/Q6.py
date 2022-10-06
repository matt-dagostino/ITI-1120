#------------------------------------------------
# Assignment 1 - Question 6 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console


n = int(input("Enter the amount of numbers would you like to input: ")) #Asks for number (n)
numbers =[] # Create list for numbers inputed

for i in range(0,n): #Loop until how many times the user wants
    num = (float(input(str(i+1) + ") Enter a number: "))) #Ask to enter number, store it in 'num' variable
    numbers.append(num) # Add num to the list 'numbers'

print() # Print an empty line
#---------------------------- Calculate Average ------------------------------
ans = 0 # Set answer to 0
for i in range(0,n): # Loop for all the numbers inputted
    ans = ans + numbers[i] #Calculate sum of numbers
ans = ans / n  #Calculate average (sum/numbers)
print("Average:",ans) #Print average

#---------------------------- Calculate Mode ------------------------------
from statistics import multimode #Import multimode from statistics (easily find mode/multiple modes)
mode = multimode(numbers) #Find mode in list
mode = sorted(mode) #Sort the list (smallest to biggest)
print("Mode: ", end = "") #Print mode title
print(*mode, sep=", ") #Print the mode(s)

#---------------------------- Calculate Median ------------------------------
sorted_list = sorted(numbers) #Sort the numbers list from smallest to biggest
middle = n // 2 # Find the middle of the list
if n % 2 == 0: #If the middle between two numbers
    median = (sorted_list[middle] + sorted_list[middle-1])/2 #Find the median
else: # If the middle is a number
    median = sorted_list[middle] #Set the median to the middle number
print("Median: " + format(median, '.3f')) #Print the median (rounded ".3f")

#---------------------------- Calculate Range ------------------------------
range = sorted_list[len(sorted_list)-1] - sorted_list[0] #Biggest number in list - smallest number, store the answer in variable called range
print("Range:", range) #Print the range