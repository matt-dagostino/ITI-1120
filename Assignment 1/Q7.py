#------------------------------------------------
# Assignment 1 - Question 7 - Matteo Dagostino
#------------------------------------------------

from operator import truediv
import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

a = [0.0, 1.0, 2.1, 1.45] #Defaulted values from an example from the assignment for easy testing
b = [0.0, 2.2, 4.32, 3.3] #Defaulted values from an example from the assignment for easy testing
c = [0.0, -1.0, 2.12, 1.1] #Defaulted values from an example from the assignment for easy testing
d = [0.0, -4.058, 8.266, 3.999] #Defaulted values from an example from the assignment for easy testing

for i in range(1,4): #Loop 3 times
    print(str(i) + ") Input the following information for ax + by + cz = d") #Print information for user
    print() #Print empty line
    a[i] = float(input("Input a: ")) #Ask for input
    b[i] = float(input("Input b: ")) #Ask for input
    c[i] = float(input("Input c: ")) #Ask for input
    d[i] = float(input("Input d: ")) #Ask for input
    print("Input received! ----> " + str(a[i]) + "x + " + str(b[i]) + "y + " + str(c[i]) + "z = " + str(d[i])) #Confirms the input received
    print("-------------------------------------------") #Print divider line

denominator = a[1]*b[2]*c[3]+b[1]*c[2]*a[3]+c[1]*a[2]*b[3]-(b[1]*a[2]*c[3]+a[1]*c[2]*b[3]+c[1]*b[2]*a[3]) #Find the denominator for the answer (Cramer's rule)
x_top = d[1]*b[2]*c[3]+b[1]*c[2]*d[3]+c[1]*d[2]*b[3]-(b[1]*d[2]*c[3]+d[1]*c[2]*b[3]+c[1]*b[2]*d[3]) #Find the numerator for x (Cramer's rule)
y_top = a[1]*d[2]*c[3]+d[1]*c[2]*a[3]+c[1]*a[2]*d[3]-(d[1]*a[2]*c[3]+a[1]*c[2]*d[3]+c[1]*d[2]*a[3]) #Find the numerator for y (Cramer's rule)
z_top = a[1]*b[2]*d[3]+b[1]*d[2]*a[3]+d[1]*a[2]*b[3]-(b[1]*a[2]*d[3]+a[1]*d[2]*b[3]+d[1]*b[2]*a[3]) #Find the numerator for z (Cramer's rule)

if x_top == y_top or x_top == z_top or y_top == z_top: #If any of the numerator values are equal to each other, then,
    if a[2]/a[1] == b[2]/b[1] and b[2]/b[1] == c[2]/c[1] and d[2]/d[1] == c[2]/c[1] or a[3]/a[1] == b[3]/b[1] and b[3]/b[1] == c[3]/c[1] and d[3]/d[1] == c[3]/c[1] or a[3]/a[2] == b[3]/b[2] and b[3]/b[2] == c[3]/c[2] and d[3]/d[2] == c[3]/c[2]: #Check to see if there are infinite number of answers
        print("There are infinite number of answers!") #Print infinite number of answers
        print() #Print empty line
    else: #If there arent infinite number of answers, then,
        print("No answer found!") #Print no answer found
        print() #Print empty line
    exit() #Exit the program

if denominator != 0: #If x,y,z can be devided by a number (not 0), then,
    x = (x_top / denominator) #Find x
    y = (y_top / denominator) #Find y
    z = (z_top / denominator) #Find z
    print("x = " + str(round(x,2))) #Print answer (x)
    print("y = " + str(round(y,2))) #Print answer (y)
    print("z = " + str(round(z,2))) #Print answer (z)
print() #Print empty line