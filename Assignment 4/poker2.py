#------------------------------------------------
#              Assignment 4 - Poker
#           Matteo Dagostino 300287930
#               mdago035@uottawa.ca
#------------------------------------------------
import random
import math
import string
import os # Makes next line work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

class Card:
  presetRank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  presetSuit = ['D', 'C', 'S', 'H']

  def __init__ (self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __str__ (self):
    if self.rank == 10:
      rank = "T"
    elif self.rank == 11:
      rank = 'J'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 1:
      rank = 'A'
    else:
      rank = self.rank
    return str(rank) + self.suit

  def __eq__ (self, other): # Equal to
    return (self.rank == other.rank)
  def __ne__ (self, other): # Not Equal to
    return (self.rank != other.rank)
  def __ge__ (self, other): # Greater than or equal
    return (self.rank >= other.rank)
  def __le__ (self, other): # Less than or equal
    return (self.rank <= other.rank)
  def __gt__ (self, other): # Greater than
    return (self.rank > other.rank)
  def __lt__ (self, other): # Less than
    return (self.rank < other.rank)
   

class cardDeck:
  def __init__ (self):
    self.cardDeck = []
    for suit in Card.presetSuit:
      for rank in Card.presetRank:
        card = Card(rank, suit)
        self.cardDeck.append(card)

  def shuffle (self):
    random.shuffle(self.cardDeck)

  def addCard(self):
    return self.cardDeck.pop(0)

class Poker:
  def __init__ (self, numPlayers):
    self.cardDeck = cardDeck()
    self.cardDeck.shuffle()
    self.hand = []
    numCards = 5

    for i in range(numPlayers):
      hand = []
      for j in range (numCards):
        hand.append(self.cardDeck.addCard())
      self.hand.append(hand)
  
  def printHands(self):
    for i in range(0, 2):
      sortedHand = sorted(self.hand[i])
      print("Hand " + str(i+1), end = ": ")

      for card in sortedHand:
        print(card, end= " ")
      print()
 
  def start(self, hand):
    self.isStraightFlush(sorted(hand))

  def isStraightFlush(self, hand):
    pass

  def isFourOfAKind(self, hand):                 
    pass
    
  def isFullHouse(self, hand):                     
    pass

  def isFlush(self, hand):                        
    pass

  def isStraight(self, hand):                        
    pass
        
  def isThreeOfAKind(self, hand):
    pass
    
  def isTwoPairs(self, hand):                          
    pass
      
  def isOnePair(self, hand):                          
    pass

  def isHighCard(self, hand):                      
    pass
    
# Main program
numPlayers = 2
startRound = Poker(numPlayers)
startRound.printHands()
startRound.start(startRound.hand)