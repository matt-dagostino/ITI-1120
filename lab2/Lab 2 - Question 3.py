x = int(input('Enter a non-negative integer: ')) #Ask to enter non-negative integer
reverse = 0 #Set default reverse

while x != 0: #Do loop while the number entered is not 0
    number = x  % 10 #Make a variable(number) and make it equal to the modulo of x / 10
    x = int(x / 10)
    reverse = reverse * 10 + number

print("The reverse is: " + str(reverse)) #Print reverse
