import os
os.system('cls' if os.name == 'nt' else 'clear')

n = int(input("Input the first positive integer: "))
k = int(input("Input the second positive integer: "))

list_k = []
temp = k
length = len(str(k))
final_list = []

while k != 0:
    list_k.insert(0, k % 10)
    k = k // 10

for i in range(1,n+1):
    list_n = []
    matches = 0
    number = int(input("(" + str(i) + "/" + str(n) + ") Input a number : " ))
    tempNumber = number
    while tempNumber != 0:
        list_n.insert(0, tempNumber % 10)
        tempNumber = tempNumber // 10
    for j in range(0,length):
        if len(str(number)) >= length:
            if list_k[j] == list_n[j]:
                matches = matches + 1
    if matches == length:
        final_list.append(number)

print("Answers: ")
print(*final_list, sep=' ')