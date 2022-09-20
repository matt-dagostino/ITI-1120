a = int(input('Enter the first number : '))
q = int(input('Enter the second number : '))
n = int(input('Enter the third number : '))

multiplication = a
answer = [a]

for i in range(1,n):

    multiplication = multiplication * q
    answer.append(multiplication) 

print(str(answer))