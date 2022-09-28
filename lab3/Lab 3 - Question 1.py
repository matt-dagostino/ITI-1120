import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console


a = int(input("Input the first integer: ")) #Asks for input
b = int(input("Input the second integer: ")) #Asks for input

print() #Print empty line
print("Primes = ", end = "") #Print start of line
primeNumbers = 0

for i in range(a, b+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime and i != 1:
        primeNumbers += 1
        print(i, end = " ")

print()
print("Number of primes = " + str(primeNumbers), "\n")
