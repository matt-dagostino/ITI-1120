x = int(input('Enter a positive integer: ')) #Ask user for input

if x == 1:
    print(x)
elif x != 1:
    print(x, end = ", ")

while x != 1: #Do while x is not equal to 1
    if x % 2 == 0: #if remainder of x is 0 then,
        x = x/2
        if x == 1:
            print(int(x))
        elif x != 1:
         print(int(x), end = ", ")
    elif x % 2 == 1: #if remainder of x is 1 then,
        x = 3*x + 1
        print(int(x), end = ", ")
