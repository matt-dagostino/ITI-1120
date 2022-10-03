import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

a = int(input("Input a positive integer greater than 1: ")) #Asks for input
is_prime = True
is_prime2 = True
numbers = []
numbers2 = []

for i in range(2,a):
    if a % i == 0:
        is_prime = False


if is_prime:
    print(a)
elif not is_prime:
    for i in range(2, a):
        if a % i == 0:
            numbers.append(i)

for i in range(0, len(numbers)):
    is_prime2 = True
    if numbers[i] == 2:
        numbers2.append(numbers[i])
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0 and numbers[i] != j:
            is_prime2 = False 
        if is_prime2 and j == numbers[i] -1:
            numbers2.append(numbers[i])
            break

answer = 1
for i in range(0, len(numbers2)):
    answer = numbers2[i] * answer
    print(answer)
    if answer == a:
        break


print(numbers)
print(numbers2)

