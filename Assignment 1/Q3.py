import os
from re import T
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

x = float(input("Enter the x value: "))
n = int(input("Enter the n value: "))

cosx = float(1)
sinx = float(x)

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans

j=2
for i in range(2,1+2*(n-1), 2):
    if j % 2 == 0:
        cosx = cosx - ((x ** i)/factorial(i))
    else:
        cosx = cosx + ((x ** i)/factorial(i))
    j +=1


j=2
for i in range(3,1+2*(n), 2):
    if j % 2 == 0:
        sinx = sinx - ((x ** i)/factorial(i))
    else:
        sinx = sinx + ((x ** i)/factorial(i))
    j +=1


print("Sin(" + str(x) + ") = " + format(sinx, '.20f'))
print("Cos(" + str(x) + ") = " + format(cosx, '.20f'))
