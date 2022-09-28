x = int(input('Enter a positive integer: ')) #Ask user for input
list = [x]

while x != 1:
    if x % 2 == 0:
        x = x/2
        list.append(int(x))
    elif x % 2 == 1:
        x = 3*x + 1
        list.append(int(x))

print(str(list))