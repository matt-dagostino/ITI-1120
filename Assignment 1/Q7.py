#------------------------------------------------
# Assignment 1 - Question 7 - Matteo Dagostino
#------------------------------------------------

from operator import truediv
import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

a = [0.0, 1.0, 2.1, 1.45]
b = [0.0, 2.2, 4.32, 3.3]
c = [0.0, -1.0, 2.12, 1.1]
d = [0.0, -4.058, 8.266, 3.999]

for i in range(1,4):
    a[i] = float(input("(x) Input a: "))
    b[i] = float(input("(y) Input b: "))
    c[i] = float(input("(z) Input c: "))
    d[i] = float(input("Input d: "))
    print("Input received! Formula " + str(i) + " = " + str(a[i]) + "x + " + str(b[i]) + "y + " + str(c[i]) + "z = " + str(d[i]))

denominator = (a[1]*((b[2])*(c[3])-(b[1])*(c[2])))-(a[2]*((b[3])*(c[3])-(b[1])*(c[1])))-(a[3]*((b[1])*(c[2]-(b[2])*(c[1]))))
x_top = (d[1]*((b[2])*(c[3])-(b[1])*(c[2])))-(d[2]*((b[3])*(c[3])-(b[1])*(c[1])))-(d[3]*((b[1])*(c[2]-(b[2])*(c[1]))))


denominator = a[1]*b[2]*c[3]+b[1]*c[2]*a[3]+c[1]*a[2]*b[3]-(b[1]*a[2]*c[3]+a[1]*c[2]*b[3]+c[1]*b[2]*a[3])
x_top = d[1]*b[2]*c[3]+b[1]*c[2]*d[3]+c[1]*d[2]*b[3]-(b[1]*d[2]*c[3]+d[1]*c[2]*b[3]+c[1]*b[2]*d[3])
y_top = a[1]*d[2]*c[3]+d[1]*c[2]*a[3]+c[1]*a[2]*d[3]-(d[1]*a[2]*c[3]+a[1]*c[2]*d[3]+c[1]*d[2]*a[3])
z_top = a[1]*b[2]*d[3]+b[1]*d[2]*a[3]+d[1]*a[2]*b[3]-(b[1]*a[2]*d[3]+a[1]*d[2]*b[3]+d[1]*b[2]*a[3])


print("------- Answer -------")
if x_top == y_top or x_top == z_top or y_top == z_top:
    if a[2]/a[1] == b[2]/b[1] and b[2]/b[1] == c[2]/c[1] and d[2]/d[1] == c[2]/c[1] or a[3]/a[1] == b[3]/b[1] and b[3]/b[1] == c[3]/c[1] and d[3]/d[1] == c[3]/c[1] or a[3]/a[2] == b[3]/b[2] and b[3]/b[2] == c[3]/c[2] and d[3]/d[2] == c[3]/c[2]:
        print("There are infinite number of answers!")
        print()
    else:
        print("No answer found!")
        print()
    exit()



if denominator != 0:
    x = (x_top / denominator)
    y = (y_top / denominator)
    z = (z_top / denominator)
    print("x = " + str(round(x,2)))
    print("y = " + str(round(y,2)))
    print("z = " + str(round(z,2)))
print()