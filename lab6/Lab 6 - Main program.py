#------------------------------------------------
# Lab 6 - Main Program - Matteo Dagostino
#------------------------------------------------

import os
from reprlib import recursive_repr #Import for next line to work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

name = str(input("Enter your name: "))
amount = float(input("Enter the amount to e-transfer: "))
recipient = str(input("Enter the recipient's name: "))
security = str(input("Enter your security question: "))
securityAnswer = str(input("Enter the security question's answer: "))

print("-----------------------------------------------------------------------")
accept = str(input(str(recipient) + ", you have received $" + str(amount) + " from " + str(name) + " via e-transfer, do you accept? "))
accept = accept.lower()

if accept == "n" or accept == "no":
    print("-----------------------------------------------------------------------")
    print(str(name) + ", your e-transfer has been declined by " + str(recipient) + ".")
elif accept == "y" or accept == "yes":
    print("-----------------------------------------------------------------------")
    verification = str(input("Security Question: " + security + " "))
    verification = verification.lower()
    securityAnswer = securityAnswer.lower()
    if securityAnswer == verification:
        print("-----------------------------------------------------------------------")
        print("The security question's answer is correct, the money has been deposited into your account.")
    elif securityAnswer != verification:
        print("-----------------------------------------------------------------------")
        print("Sorry, the security question's answer is wrong, the money has been returned to " + str(name) + ".")
print()