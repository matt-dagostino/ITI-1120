#------------------------------------------------
# Midterm 1 - Question 3 - Matteo Dagostino
#------------------------------------------------

import os #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console
list = []

for i in range(0, int(input("Enter the amount of words that you want to enter: "))):
    list.append(str(input("Enter a word: ")))
#list = ["Bahrami", "Dingding", "HuHuHu", "Rahim", "Python", "189a189a189a", "901xyx109"]


def is_boring(listInput):
    new_list = []
    for word in listInput:
        word2 = word.lower()
        for i in range(2,len(word2)):
            if len(word2) % i == 0:
                #print(word, i)
                x = int(len(word2)/i)
                y = ""
                for h in range(0,x):
                    y = y + word2[h]
                repeat = True
                for k in range(0, x):
                    if y[k] != word2[k+x]:
                        repeat = False
                        break
                if repeat == True:
                    new_list.append(word)
    return new_list

print("-------------------------------------- Output --------------------------------------")
print(' '.join(is_boring(list)))