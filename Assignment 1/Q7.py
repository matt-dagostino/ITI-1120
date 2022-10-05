#------------------------------------------------
# Assignment 1 - Question 7 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

a = [0.0, 1.0, 2.1, 1.45]
b = [0.0, 2.2, 4.32, 3.3]
c = [0.0, -1.0, 2.12, 1.1]
d = [0.0, -4.058, 8.266, 3.899]

denominator = a[1]*((b[2])*(c[3])-(b[1])*(c[2]))-a[2]*((b[3])*(c[3])-(b[1])*(c[1]))-a[3]*((b[1])*(c[2]-(b[2])*(c[1])))
x_top = d[1]*((b[2])*(c[3])-(b[1])*(c[2]))-d[2]*((b[3])*(c[3])-(b[1])*(c[1]))-d[3]*((b[1])*(c[2]-(b[2])*(c[1])))
print(x_top / denominator)