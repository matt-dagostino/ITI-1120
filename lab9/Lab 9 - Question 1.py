#------------------------------------------------
# Lab 9 - Question 1 - Matteo Dagostino
#------------------------------------------------

import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
codingClass = []

class GradeManager:
    def __init__(self, firstname, lastname, labs, assignment1, assignment2, assignment3, assignment4, assignment5, term_test, midterm, final):
        self.firstname = firstname
        self.lastname = lastname
        self.labs = labs
        self.assignment1 = ((assignment1/30)*100)*0.05
        self.assignment2 = ((assignment2/30)*100)*0.05
        self.assignment3 = ((assignment3/30)*100)*0.05
        self.assignment4 = ((assignment4/30)*100)*0.05
        self.assignment5 = ((assignment5/30)*100)*0.05
        self.term_test = term_test
        self.midterm = midterm
        self.final = final
        self.final_mark = self.labs + self.assignment1+ self.assignment2+ self.assignment3+ self.assignment4+ self.assignment5 + self.term_test + self.midterm + self.final
        
        if self.final_mark >= 90:
            self.letter_grade = "A+"
        elif self.final_mark < 90 and self.final_mark >= 85:
            self.letter_grade = "A"
        elif self.final_mark < 85 and self.final_mark >= 80:
            self.letter_grade = "A-"
        elif self.final_mark < 80 and self.final_mark >= 75:
            self.letter_grade = "B+"
        elif self.final_mark < 75 and self.final_mark >= 70:
            self.letter_grade = "B"
        elif self.final_mark < 70 and self.final_mark >= 65:
            self.letter_grade = "C+"
        elif self.final_mark < 65 and self.final_mark >= 60:
            self.letter_grade = "C"
        elif self.final_mark < 60 and self.final_mark >= 55:
            self.letter_grade = "D+"
        elif self.final_mark < 55 and self.final_mark >= 50:
            self.letter_grade = "D"
        elif self.final_mark < 50 and self.final_mark >= 40:
            self.letter_grade = "E"
        elif self.final_mark < 40:
            self.letter_grade = "F"

for i in range(0, int(input("Enter the amount of students: "))):
    studentName = str(input("Enter the student's name: "))
    first_last = studentName.split()
    x = str(input("Enter the grades: "))
    list = x.split()
    codingClass.append(GradeManager(first_last[0], first_last[1], float(list[0]), float(list[1]), float(list[2]), float(list[3]), float(list[4]), float(list[5]), float(list[6]), float(list[7]), float(list[8])))


print("----------------------------------------------------------------")
studentNumber = 1
for i in codingClass:
    print("Student " + str(studentNumber) + ":")
    print("---> Firstname: " + i.firstname)
    print("---> Lastname: " + i.lastname)
    print("---> Lab mark: " + str(i.labs) + "%")
    print("---> Assignment 1: " + str(round(i.assignment1, 2)) + "%")
    print("---> Assignment 2: " + str(round(i.assignment2, 2)) + "%")
    print("---> Assignment 3: " + str(round(i.assignment3, 2)) + "%")
    print("---> Assignment 4: " + str(round(i.assignment4, 2)) + "%")
    print("---> Assignment 5: " + str(round(i.assignment5, 2)) + "%")
    print("---> Term test: " + str(i.term_test) + "%")
    print("---> Miderm: " + str(i.midterm) + "%")
    print("---> Final exam: " + str(i.final) + "%")
    print("---> Final mark: " + str(round(i.final_mark, 2)) + "%")
    print("---> Letter Grade: " + str(i.letter_grade))
    studentNumber = studentNumber + 1
