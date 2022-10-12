#------------------------------------------------
# Lab 5 - Question 1 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

n = int(input("Enter a positive integer: "))

def findDivisors(number):
    divisors = []
    for i in range(1,n):
        if number % i == 0:
            divisors.append(i)
    return divisors

def addDivisors(list):
    answer = 0
    for i in range(0,len(list)):
        answer = answer + list[i]
    return answer

if addDivisors(findDivisors(n)) == n:
    print(n, "is a complete number.")
else:
    print(n, "is not a complete number.")

print()
