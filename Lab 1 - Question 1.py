# Matteo Dagostino - September 15

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
print('---------------------------------')
if a > b and a > c:
    if b > c:
        print('The Largest Value is : ' + str(a) + str(b) + str(c))
        if c == 0:
            print('The Smallest Value is : ' + str(b) + str(a))
        else:
            print('The Smallest Value is : ' + str(c) + str(b) + str(a))
    elif c > b:
        print('The Largest Value is : ' + str(a) + str(c) + str(b))
        if b == 0:
            print('The Smallest Value is : ' + str(c) + str(a))
        else:
            print('The Smallest Value is : ' + str(b) + str(c) + str(a))
elif b > a and b > c:
    if a > c:
        print('The Largest Value is : ' + str(b) + str(a) + str(c))
        if c == 0:
            print('The Smallest Value is : ' + str(a) + str(b))
        else:
            print('The Smallest Value is : ' + str(c) + str(a) + str(b))
    elif c > a:
        print('The Largest Value is : ' + str(b) + str(c) + str(a))
        if a == 0:
            print('The Smallest Value is : ' + str(c) + str(b))
        else:
            print('The Smallest Value is : ' + str(a) + str(c) + str(b))
elif c > a and c > b:
    if b > a:
        print('The Largest Value is : ' + str(c) + str(b) + str(a))
        if a == 0:
            print('The Smallest Value is : ' + str(b) + str(c))
        else:
            print('The Smallest Value is : ' + str(a) + str(b) + str(c))
    elif a > b:
        print('The Largest Value is : ' + str(c) + str(a) + str(b))
        if b == 0:
            print('The Smallest Value is : ' + str(a) + str(c))
        else:
            print('The Smallest Value is : ' + str(b) + str(a) + str(c))
elif a == b and a == c:
    print('The Largest Value is : ' + str(c) + str(c) + str(c))
    print('The Smallest Value is : ' + str(c) + str(c) + str(c))
elif a == b:
    if c > a:
        print('The Largest Value is : ' + str(c) + str(a) + str(a))
        if a == 0:
            print('The Smallest Value is : ' + str(c))
        else:
            print('The Smallest Value is : ' + str(a) + str(a) + str(c))
    elif c < a:
        print('The Largest Value is : ' + str(a) + str(a) + str(c))
        print('The Smallest Value is : ' + str(c) + str(a) + str(a))
elif c == b:
    if a > c:
        print('The Largest Value is : ' + str(a) + str(c) + str(c))
        if c == 0:
            print('The Smallest Value is : ' + str(a))
        else:
            print('The Smallest Value is : ' + str(c) + str(c) + str(a))
    elif a < c:
        print('The Largest Value is : ' + str(c) + str(c) + str(a))
        print('The Smallest Value is : ' + str(a) + str(c) + str(c))
elif a == c:
    if b > a:
        print('The Largest Value is : ' + str(b) + str(a) + str(a))
        if a == 0:
            print('The Smallest Value is : ' + str(b))
        else:
            print('The Smallest Value is : ' + str(a) + str(a) + str(b))
    elif b < a:
        print('The Largest Value is : ' + str(a) + str(a) + str(b))
        if b == 0:
            print('The Smallest Value is : ' + str(a) + str(a))
        else:
            print('The Smallest Value is : ' + str(b) + str(a) + str(a))

else:
    print("Error")
