#------------------------------------------------
#              Assignment 4 - Poker
#           Matteo Dagostino 300287930
#               mdago035@uottawa.ca
#------------------------------------------------
import random
import os # Makes next line work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

# Defining variables
players = 2
deck = []
ranks = ["A", "2","3","4","5","6","7","8","9","T","J","Q","K"]
suits = ["D", "C", "S", "H"]

for suit in suits:
    for rank in ranks:
        deck.append(rank+suit)

class Poker:
    def __init__(self, player):
        self.playerName = player
        self.cards = []
        random.shuffle(deck)

    def add_card(self, deck):
        self.cards.append(deck[0])
        deck.pop(0)

    def add_to_table(self, deck):
        print(deck[0] + " has been placed on the table")
        deck.pop(0)
    
    def IsFlush(self):
        if "H" in self.cards[0] and "H" in self.cards[1] and "H" in self.cards[2] and "H" in self.cards[3] and "H" in self.cards[4]:
            return True
        elif "C" in self.cards[0] and "C" in self.cards[1] and "C" in self.cards[2] and "C" in self.cards[3] and "C" in self.cards[4]:
            return True
        elif "S" in self.cards[0] and "S" in self.cards[1] and "S" in self.cards[2] and "S" in self.cards[3] and "S" in self.cards[4]:
            return True
        elif "D" in self.cards[0] and "D" in self.cards[1] and "D" in self.cards[2] and "D" in self.cards[3] and "D" in self.cards[4]:
            return True
        else:
            return False
        
    def IsStraightFlush(self):
        if "H" in self.cards[0] and "H" in self.cards[1] and "H" in self.cards[2] and "H" in self.cards[3] and "H" in self.cards[4]:
            return True
        elif "C" in self.cards[0] and "C" in self.cards[1] and "C" in self.cards[2] and "C" in self.cards[3] and "C" in self.cards[4]:
            return True
        elif "S" in self.cards[0] and "S" in self.cards[1] and "S" in self.cards[2] and "S" in self.cards[3] and "S" in self.cards[4]:
            return True
        elif "D" in self.cards[0] and "D" in self.cards[1] and "D" in self.cards[2] and "D" in self.cards[3] and "D" in self.cards[4]:
            return True
        else:
            return False

    def show(self):
        print(self.cards)
    
    def set(self):
        self.cards.append("1H")
        self.cards.append("2H")
        self.cards.append("3H")
        self.cards.append("4H")
        self.cards.append("5H")

playerCards = []
x = int(input("How many players are there? "))
for i in range(0, x):
    playerCards.append(Poker(i))

    

# if p1.IsFlush() == True:
#     print("Flush")