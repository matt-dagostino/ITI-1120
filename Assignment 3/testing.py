import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

while 1 > 0:
    test= str(input("Enter: "))

    te = ''.join(test.split())

    print(te)