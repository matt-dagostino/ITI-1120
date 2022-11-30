#------------------------------------------------
# Lab 11 - Question 1 - Matteo Dagostino
#------------------------------------------------
import math
import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console


# Pre made functions ---------------------------------
def sumIntegers(n): # Adds all numbers from 1 to n
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sequence(n): #If divisable, divide by 2, else times 3 + 1
    seq = []
    while n != 1:
        seq.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    seq.append(1)
    return seq

def check(word): #Check if word is just same letter repeated
    n = len(word)
    i = 0
    j = n-1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1
    return True

# Recursive functions ---------------------------------
def integerSum(n):
    if n == 0:
        return 0
    else:
        return n + integerSum(n-1)

def sequencing(n, seq):
    seq.append(n)
    if n == 1:
        return seq
    else:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return sequencing(n, seq)

def checkWord(word):
    if len(word) > 1:
        i = 0
        n = len(word)
        j = n-1
        if word[i] != word[j]:
            return False
        else:
            return checkWord(word[:-1])
    return True

x = int(input("Enter number for sum and sequence: "))
y = str(input("Enter word for check word: "))

#Printing outputs
print("\nNon-Recursive Functions: ")
print("Sum Integers: " + str(sumIntegers(x)))
print("Sequence: " + str(sequence(x)))
print("Word: " + str(check(y)))
#---------------------------------
print("\nRecursive Functions: ")
print("Sum Integers: " + str(integerSum(x)))
print("Sequence: " + str(sequencing(x, [])))
print("Word: " + str(checkWord(y)) + "\n")