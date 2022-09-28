import os
os.system('cls' if os.name == 'nt' else 'clear')


a = int(input("Input the first integer: "))
b = int(input("Input the second integer: "))

print("Primes = ", end = "")
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
print("Number of primes = " + str(primeNumbers))




# n = int(input('Enter a positive integer: '))
# is_prime = True

# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime:    # is_prime == True
#     print('The number is prime', end = ', ')
# else:
#     print('The number is not prime', end = ', ')
    
# print('end of the program')

