#------------------------------------------------
# Midterm 1 - Question 2 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system("cls" if os.name == "nt" else "clear") # Clears the console
A = {}
B = {}



for i in range(0, int(input("Enter the amount of midterm grades that would you like to add: "))):
    name = str(input("Enter name: "))
    grade = int(input("----> Enter grade: "))
    A[name] = grade

print("--------------------------------------")
for i in range(0, int(input("Enter the amount of final grades that would you like to add: "))):
    name = str(input("Enter name: "))
    grade = int(input("----> Enter grade: "))
    B[name] = grade


A = { "Mike Armstrong" : 35, "Zoey James": 38, "Martin Max": 27, "Albert Wesker": 31 }
B = { "Hannah Tan" : 51, "Zoey James": 46, "Martin Max": 55, "Albert Wesker": 40 }

def combine(midterm, final):
    endGrade = {}
    for key, value in midterm.items():
        for key2,value2 in final.items():
            if key in final:
                if key == key2:
                    endGrade[key] = value + value2
                    break
            else:
                endGrade[key] = 0
    for key2,value2 in final.items():
            if key2 in midterm:
                break
            else:
                endGrade[key2] = value2
            
    return endGrade

print("-------------------------------------- Output --------------------------------------")
print(combine(A,B))
print()
        