#------------------------------------------------
# Midterm 1 - Question 5 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

def get_inputs(): #Create function to get inputs
    list = [] #Create empty list
    for i in range(0, int(input("Enter the amount of numbers that you want to input: "))): #Loop for the amount of numbers that will be entered
        list.append(float(input("Enter a number: "))) #Add entered number to list
    return list #Return list

list1 = get_inputs() #Get input for list1
list2 = get_inputs() #Get input for list2

def smaller(A, B): #Create function to check which number is smaller
    if A > B: #If b is smaller, then
        return B #Return B
    elif B > A: #If a is smaller, then
        return A #Return A
    elif B == A: #If b is equal to a, then
        return A #Return A

def sort(A, B): #Create function to sort lists
    sorted = [] #Create empty list
    i = 0 #Set i to 0
    j = 0 #Set j to 0
    while i < len(A) and j < len(B): #Do while i is smaller than length of A and j is smaller than length of B
        x = smaller(A[i], B[j]) #x is the smaller value between A[i] and B[j]
        sorted.append(x) #Add x to list
        if x == A[i] and x == B[j]: #If numbers are equal
            i = i + 1 #Add 1 to i
            j = j + 1 #Add 1 to j
            sorted.append(x) #Add x to list
        elif x == A[i]: #If a is smallest value
            i = i + 1 #Add 1 to i 
        elif x == B[j]: #If b is smallest value
            j = j + 1 #Add 1 to j
    if len(A) > i: #If length of A is bigger than i
        for m in range(i, len(A)): #Loop from i to length of list A
            sorted.append(A[m]) #Add to list
    elif len(B) > i: #If length of B is bigger than i
        for m in range(i, len(B)): #Loop from i to length of list B
            sorted.append(B[m]) #Add to list
    elif smaller(len(A), len(B)) == len(A): #If A is smallest list
        sorted.append(B[len(B)-1]) #Add to list
    elif smaller(len(A), len(B)) == len(B): #If B is smallest list
        sorted.append(A[len(A)-1]) #Add to list

    return sorted #Return final list

print("-------------------------------------- Output --------------------------------------") #Print divider
print(sort(list1, list2)) #Print output
print() #Print empty line