#------------------------------------------------
# Lab 5 - Question 2 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
import math

n = int(input("Enter a positive integer: "))

numbers = []
for i in range(0,n):
    numbers.append(float(input(str(i+1) + ") Enter a number: ")))

def getAverage(terms, numberterms):
    sum = 0
    for i in range(0, numberterms):
        sum = sum + terms[i]
    return sum/numberterms

def nominator(terms, average):
    nominatorNumber = 0
    for i in range(0,len(terms)):
        nominatorNumber = nominatorNumber + math.pow(terms[i]-average,2)
    return nominatorNumber

def SD(nominator, n):
    standardDeviation = math.sqrt(nominator/n)
    return standardDeviation

print("The standard deviation is " + str(SD(nominator(numbers, getAverage(numbers,n)),n)))
print()