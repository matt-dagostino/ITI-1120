# Matteo Dagostino - September 15

print('The equation is the following: y = mx + b, enter the following values :')
m = float(input("m = "))
b = float(input("b = "))
print('A point can be known as (x,y), enter the following values :')
x = float(input("x = "))
y = float(input("y = "))

testing = (y-b)/m

if testing < x:
    print('Your point is located to the right of the line')
elif testing > x:
    print('Your point is located to the left of the line')
else:
    print('Your point is located on the line')
