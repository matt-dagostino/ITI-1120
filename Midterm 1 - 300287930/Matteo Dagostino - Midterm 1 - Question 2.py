#------------------------------------------------
# Midterm 1 - Question 2 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system("cls" if os.name == "nt" else "clear") # Clears the console
A = {} #Create empty dictionary (A)
B = {} #Create empty dictionary (B)

for i in range(0, int(input("Enter the amount of midterm grades that would you like to add: "))): #Loop for the amount of numbers to be entered
    name = str(input("Enter name: ")) #Ask user for name
    grade = int(input("----> Enter grade: ")) #Ask user for grade
    A[name] = grade #Add to dictionary (A)

print("--------------------------------------") #Print divider
for i in range(0, int(input("Enter the amount of final grades that would you like to add: "))): #Loop for the amount of numbers to be entered
    name = str(input("Enter name: ")) #Ask user for name
    grade = int(input("----> Enter grade: ")) #Ask user for grade
    B[name] = grade#Add to dictionary (B)

def combine(midterm, final): #Define function called combine(dictionary, dictionary)
    endGrade = {} #Create dictionary for final results
    for key, value in midterm.items(): #For name, grade in midterm
        for key2,value2 in final.items(): #For name, grade in final
            if key in final: #Check if the person did the final, if yes, then
                if key == key2: #Find the name in both lists
                    endGrade[key] = value + value2 #Add the values together
                    break # End loop
            else: #If person did not do the final, then
                endGrade[key] = 0 #Set their grade to 0
    for key2,value2 in final.items(): #For name, grade in final
            if key2 in midterm: #If they did midterm then,
                l = 1 #does nothing (placeholder)
            else: #If they didnt do the midterm, then
                endGrade[key2] = value2 #Set final result to grade from final
    return endGrade #Return results

print("-------------------------------------- Output --------------------------------------") #Print divider
print(combine(A,B)) #Call function, print returned value
print() #Print empty line
        