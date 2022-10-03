import os # Imports os for the next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

n = int(input("Enter the number in base 10: ")) #Asks for number
b = int(input("Enter the base wanted: ")) #Asks for base

remainder = [] #Creates list

while n > 0: #Do while n > 0
    remainder.append(n % b) #Add the remainder to list
    n //= b # Devide n by b

for i in range(1, len(remainder)+1): #Loop 1 to length of list +1
    j = len(remainder)-i #j = length-1 (this is to reverse the list)
    print(remainder[j], end = "") #Prints the numbers 1 by 1 (answer)