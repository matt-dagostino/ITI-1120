x = int(input('Enter a positive integer: ')) #Ask user for input
list = [x] #Create list


while x != 1: #Do while x is not equal to 1
    if x % 2 == 0: #if remainder of x is 0 then,
        x = x/2
        list.append(int(x)) #add to list
    elif x % 2 == 1: #if remainder of x is 1 then,
        x = 3*x + 1
        list.append(int(x)) #add to list

print(str(list)) #print answer