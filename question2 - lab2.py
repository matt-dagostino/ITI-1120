from audioop import mul


a = int(input('Enter the first number : '))
q = int(input('Enter the second number : '))
n = int(input('Enter the third number : '))

multiplication = a
answer = [a]

for i in range(1,n):

    multiplication = multiplication * q
    answer.append(multiplication) 


    # 2 5 7
    # 2, 10, 50, 250, 1250, 6250, 31250
print(str(answer))