a = int(input('Enter the first number : ')) #Ask for input
q = int(input('Enter the second number : ')) #Ask for input
n = int(input('Enter the third number : ')) #Ask for input

multiplication = a
answer = [a]

for i in range(1,n):

    multiplication = multiplication * q
    answer.append(multiplication) 

print(str(answer))