a = int(input('Enter an integer: '))
sum = 0

print("Divisors = ", end ="")

for i in range(1, a+1):
    if i != a:
        if a % i == 0:
            sum = sum + i
            print(i, end = ", ")
    elif i == a:
        if a % i == 0:
            sum = sum + i
            print(i)

print("Sum of divisors = " + str(sum))