#------------------------------------------------
# Midterm 1 - Question 4 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

def get_inputs(): #Create function to get inputs
    list = [] #Create empty list
    for i in range(0, int(input("Enter the amount of strings that you want to input: "))): #Loop for the amount of numbers to be entered
        list.append(str(input("Enter a string: "))) #Ask user for input and add to list
    return list #Return list

list1 = get_inputs() #Get list1
list2 = get_inputs() #Get list2

def combine(A, B): #Create function to combine lists
    found = False #Set found to False
    for i in range(0, len(list1)): #Loop from 0 to the length of list1
        if i < len(list2): # check if i is smaller than the length of list2
            if A[len(list1)-1] == B[i]: # check if the last input in list A is equal to any input in list B
                index = i # Set index to i
                for j in range(0,i): #Loop from 0, index
                    j = j + 1 #Set j to itself + 1
                    if A[(len(list1)-1)-j] == B[j-1]: #Check if item before last item is equal to item before last item in other list
                        found = True #Set found to True
                    else: #Otherwise,
                        found = False #Set found to False
    if found == True: #If found == True
        new_B = [] # Create new list for B
        for i in range(index+1, len(B)): #Loop from index +1 until length of list B
            new_B.append(B[i]) #Add B[i] to new list (new_B)
    elif found != True: #If found is False
        new_B = B #Set new_B to B
    final_list = [] #Create final_list list
    for word in A: #For each word in A list
        final_list.append(word) #Add word to final list
    for word in new_B:#For each word in new_B list
        final_list.append(word) #Add word to final list

    return final_list #Return the final list

print("-------------------------------------- Output --------------------------------------") #Print divider 
print("[" + ', '.join(combine(list1, list2))+ "]") #Call combine function and print results
print() #Print empty line

        

    