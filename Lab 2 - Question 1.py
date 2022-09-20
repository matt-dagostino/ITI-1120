a = int(input('Enter an integer: '))
sum = 0
divisors = []

for i in range(1, a+1):
    if a % i == 0:
        sum = sum + i
        divisors.append(i)

print("Divisors = " + str(divisors))
print("Sum of divisors = " + str(sum))