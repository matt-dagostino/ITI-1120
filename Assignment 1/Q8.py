#------------------------------------------------
# Assignment 1 - Question 8 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
from collections import Counter # Imports the counter function which counts 

#-------------------- Creation of lists --------------------
u =[] #Create list
a = [] #Create list
b = [] #Create list

#-------------------- Asks the user to input the sets --------------------
num = int(input("Enter the number of elements in the universal set: ")) #Asks for elements in set
for i in range(0,num): #Loop num amount
    u.append(int(input(str(i+1) + ") Enter a number: "))) #Asks for element

num = int(input("Enter the number of elements in the A set: ")) #Asks for elements in set
for i in range(0,num): #Loop num amount
    a.append(int(input(str(i+1) + ") Enter a number: "))) #Asks for element

num = int(input("Enter the number of elements in the B set: ")) #Asks for elements in set
for i in range(0,num): #Loop num amount
    b.append(int(input(str(i+1) + ") Enter a number: "))) #Asks for element


#-------------------- Sort lists --------------------
u_final = sorted(u) # ^^^^^^^
a_final = sorted(a) # ^^^^^^^
b_final = sorted(b) # ^^^^^^^

#-------------------- Calculate A Union B (1) --------------------
q1 = sorted(a_final + b_final) #Add list a and b together
q1_counted = Counter(q1).items() # Counts how many times the numbers are repeated in a list
q1_list = [] #Create list
for number, repeatedTimes in q1_counted: #Loop for list (number, repeatedTimes)
    q1_list.append(number) #Add number to list
print() #Print empty line
print("------------- Answers -------------") #Print title
print("A Union B = ", end ="") #Print answer
print(*q1_list, sep = ", ") #Print answer


#-------------------- Calculate A Intersection B (2) --------------------
q2_list = [] #Create list
for i in range(0,len(a)): #Loop from 0 to the length of list a
    for j in range(0,len(b)): #Loop from 0 to the length of list b
        if a[i] == b[j]: #If a and b are equal then,
            q2_list.append(a[i]) #Add to list
            break #Stop loop
q2_list = sorted(q2_list) #Sort list
print("A Intersection B = ", end ="") #Print answer
print(*q2_list, sep = ", ") #Print answer


#-------------------- Calculate A - B (3) --------------------
q3_list = [] #Create list
for i in range(0,len(a)): #Loop from 0 to the length of list a
 if a[i] not in q2_list: #If it (a[i]) is not found in q2_list, then,
    q3_list.append(a[i]) #Add to list
q3_counted = Counter(q3_list).items() # Counts how many times the numbers are repeated in a list
q3_final = [] #Create list
for number, repeatedTimes in q3_counted: #Loop for list (number, repeatedTimes)
    q3_final.append(number) #Add number to list
q3_final = sorted(q3_final) #Sort list
print("A - B = ", end ="") #Print answer
print(*q3_final, sep = ", ") #Print answer


#-------------------- Calculate B - A (4) --------------------
q4_list = [] #Create list
for i in range(0,len(b)): #Loop from 0 to the length of list b
 if b[i] not in q2_list: #If it (b[i]) is not found in q2_list, then,
    q4_list.append(b[i]) #Add to list
q4_counted = Counter(q4_list).items() # Counts how many times the numbers are repeated in a list
q4_final = [] #Create list
for number, repeatedTimes in q4_counted: #Loop for list (number, repeatedTimes)
    q4_final.append(number) #Add number to list
q4_final = sorted(q4_final) # Sort list
print("B - A = ", end ="") #Print answer
print(*q4_final, sep = ", ") #Print answer


#-------------------- Calculate A Complement (5) --------------------
q5_list = [] #Create list
for i in range(0,len(u)): #Loop from 0 to the length of list u
 if u[i] not in a: #If it (u[i]) is not found in a (list), then,
    q5_list.append(u[i]) #Add to list
q5_counted = Counter(q5_list).items() # Counts how many times the numbers are repeated in a list
q5_final = [] #Create list
for number, repeatedTimes in q5_counted: #Loop for list (number, repeatedTimes)
    q5_final.append(number) #Add number to list
q5_final = sorted(q5_final) #Sort list
print("A Complement = ", end ="") #Print answer
print(*q5_final, sep = ", ") #Print answer

#-------------------- Calculate B Complement (6) --------------------
q6_list = [] #Create list
for i in range(0,len(u)): #Loop from 0 to the length of list u
 if u[i] not in b: #If it (u[i]) is not found in b (list), then,
    q6_list.append(u[i]) #Add to list
q6_counted = Counter(q6_list).items() # Counts how many times the numbers are repeated in a list
q6_final = [] #Create list
for number, repeatedTimes in q6_counted: #Loop for list (number, repeatedTimes)
    q6_final.append(number) #Add number to list
q6_final = sorted(q6_final) #Sort list
print("B Complement = ", end ="") #Print answer
print(*q6_final, sep = ", ") #Print answer

#-------------------- Calculate A ^ B (7) --------------------
q7_list = q3_final + q4_final #Adds 2 lists together (q3 & q4)
q7_list = sorted(q7_list) #Sort the list
print("A ^ B = ", end ="") #Print answer
print(*q7_list, sep = ", ") #Print answer
print() #Print empty line