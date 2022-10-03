from collections import Counter # Imports the counter function which counts 
from math import * # Imports all math functions
import os # Imports os for the next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

a = int(input("Input a positive integer greater than 1: ")) #Asks for input
is_prime = True #Set boolean value to True
is_prime2 = True #Set boolean value to True
numbers = [] #Create list
numbers2 = [] #Create list

if a <= 1: #Check if input is bigger than 1
    print("ERROR: Number needs to be bigger than 1!") #Print error message
    exit() #Stop code from continuing

for i in range(2,a): #Loop from 2 to inputted number
    if a % i == 0: #Check if there is a remainder, if not, then,
        is_prime = False #Set boolean value to False

if not is_prime: #If boolean value is false, then,
    for i in range(2, a): #Loop from 2 to inputted number
        if a % i == 0: #Check if there is a remainder, if not, then,
            numbers.append(i) #Add number 'i' to list

for i in range(0, len(numbers)): #Loop from 2 to length of list 'numbers'
    is_prime2 = True #Set boolean value to True
    if numbers[i] == 2: #Check if the number is 2, then,
        numbers2.append(numbers[i]) #Add 2 to the list
    for j in range(2, numbers[i]):  #Loop from 2 to the value of numbers[index]
        if numbers[i] % j == 0 and numbers[i] != j: #If no remainder and not equal to the same number then,
            is_prime2 = False #Set boolean False
        if is_prime2 and j == numbers[i] -1: #If its prime
            numbers2.append(numbers[i]) #Add to second list
            break #Stop for loop (line 29)

productList = lcm(*numbers2) #Times the numbers in the list together (*)
numbers2.append(a // productList) # Adds the initial inputed number devided by the productList to the list of prime numbers

c = Counter(numbers2) # Counts how many times the numbers are repeated in a list
final_list = c.items() # Turns counter into a dictionary with (factorNumber, repeatedTimes)
answerString = [] # Create list called answerString

for factorNumber, repeatedTimes in final_list:
    if (factorNumber == 1): # This line is to eliminate adding "* 1" to our answer (Example: 2 * 3 * 5 * 1, this would make it, 2 * 3 * 5)
      continue # Continue function will restart the loop starting at the next iteration (to avoid 1)
      
    if (answerString): # If there is an item/variable in the list then,
      answerString.append(' * ') # Add multiplication symbol to the list (won't do it the first time since list will be empty)
      
    answerString.append(str(factorNumber)) # Add the factorNumber at its iteration to the list
    if (repeatedTimes > 1): # If that number's value appears more than once in the list then,
      answerString.append('^') # Add the exponent symbol to the answer
      answerString.append(str(repeatedTimes)) # Add the value of how many times it was repeated to the answer
  
answerString.insert(0, "The answer is : ") #Adds "The answer is : " to the beggining of the answer list

for i in range(0,len(answerString)): # Goes threw all indexes in the answer 
    print(answerString[i], end = "") # Prints every index 1 by 1