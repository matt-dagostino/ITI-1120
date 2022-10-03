from collections import Counter # Imports the counter function which counts 
from math import * # Imports all math functions
import os # Imports os for the next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

a = int(input("Input a positive integer greater than 1: ")) #Asks for input
is_prime = True
is_prime2 = True
numbers = []
numbers2 = []

for i in range(2,a):
    if a % i == 0:
        is_prime = False

if not is_prime:
    for i in range(2, a):
        if a % i == 0:
            numbers.append(i)

for i in range(0, len(numbers)):
    is_prime2 = True
    if numbers[i] == 2:
        numbers2.append(numbers[i])
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0 and numbers[i] != j:
            is_prime2 = False 
        if is_prime2 and j == numbers[i] -1:
            numbers2.append(numbers[i])
            break

prime_number_list = numbers2

productList = lcm(*prime_number_list) #Times the numbers in the list together (*)
prime_number_list.append(a // productList) # Adds the initial inputed number devided by the productList to the list of prime numbers

c = Counter(prime_number_list) # Counts how many times the numbers are repeated in a list
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