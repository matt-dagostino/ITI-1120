#------------------------------------------------
# Midterm 1 - Question 4 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

list1 = ["John", "Mike1992","Terry2000"]
list2 = ["1Rain", "Mike1992", "John56", "John"]

def combine(A, B):
    found = False
    for i in range(0, len(list1)):
        if i < len(list2):
            if A[len(list1)-1] == B[i]:
                index = i
                for j in range(0,i):
                    j = j + 1
                    if A[(len(list1)-1)-j] == B[j-1]:
                        found = True
                    else:
                        found = False
    if found == True:
        new_B = []
        for i in range(index+1, len(B)):
            new_B.append(B[i])
    elif found != True:
        new_B = B
    final_list = []
    for word in A:
        final_list.append(word)
    for word in new_B:
        final_list.append(word)

    return final_list

combine(list1, list2)
print("-------------------------------------- Output --------------------------------------")
print("[" + ', '.join(combine(list1, list2))+ "]")
print()

        

    