#------------------------------------------------
# Midterm 1 - Question 3 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
list = [] #Create empty list

for i in range(0, int(input("Enter the amount of words that you want to enter: "))): #Loop from 0 until the amount of words wanting to be entered
    list.append(str(input("Enter a word: "))) #Ask user for a word, add it to list

def is_boring(listInput): #Create functon to check if boring
    new_list = [] #Create new list
    for word in listInput: #For each word entered
        word2 = word.lower() #Set the words to lowercase
        for i in range(2,len(word2)): #Loop from 2, length of the word
            if len(word2) % i == 0: #If the length of the word is divisable
                x = int(len(word2)/i) # x = length of the word divided by i
                y = "" #Create y variable
                for h in range(0,x): #Loop from 0, x
                    y = y + word2[h] #Set y to the repeated substring (Example: "Ding" in Dingdingdingding)
                repeat = True # Set repeat to True
                for k in range(0, x): #Loop from 0, x
                    if y[k] != word2[k+x]: # If the substring isn't in the word, then
                        repeat = False #Set repeat to False
                        break  #End loop
                if repeat == True: #If repeat is True
                    new_list.append(word) #Add the word to the final list of words
    return new_list # Return final answer

print("-------------------------------------- Output --------------------------------------") #Print divider
print(' '.join(is_boring(list))) #Call function, seperate with space, print returned results
print() #Print empty line