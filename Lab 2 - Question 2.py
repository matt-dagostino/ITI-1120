a = int(input('Enter the first number : ')) #Ask for input 1
q = int(input('Enter the second number : ')) #Ask for input 2
n = int(input('Enter the third number : ')) #Ask for input 3

multiplication = a
print(multiplication, end = ", ")
for i in range(1,n):

    if i != n-1:
        multiplication = multiplication * q
        print(multiplication, end = ", ")
    if i == n-1:
        multiplication = multiplication * q
        print(multiplication)