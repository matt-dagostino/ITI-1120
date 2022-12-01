# ------------------------------------------------
#              Assignment 4 - Poker
#           Matteo Dagostino 300287930
#               mdago035@uottawa.ca
# ------------------------------------------------
import random
import math
import string
import os  # Makes next line work
os.system(('cls' if os.name == 'nt' else 'clear'))  # Clears the console


class Card:
    presetRank = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        ]
    presetSuit = ["D", "C", "S", "H"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, compared):  # Equal to
        return self.rank == compared.rank

    def __ne__(self, compared):  # Not Equal to
        return self.rank != compared.rank

    def __ge__(self, compared):  # Greater than or equal
        return self.rank >= compared.rank

    def __le__(self, compared):  # Less than or equal
        return self.rank <= compared.rank

    def __gt__(self, compared):  # Greater than
        return self.rank > compared.rank

    def __lt__(self, compared):  # Less than
        return self.rank < compared.rank

    def __str__(self):
        if self.rank == 10:
            rank = "T"
        elif self.rank == 11:
            rank = "J"
        elif self.rank == 12:
            rank = "Q"
        elif self.rank == 13:
            rank = "K"
        elif self.rank == 1:
            rank = "A"
        else:
            rank = self.rank
        return str(rank) + self.suit

class cardDeck:
    def __init__(self):
        self.cardDeck = []
        for suit in Card.presetSuit:
            for rank in Card.presetRank:
                card = Card(rank, suit)
                self.cardDeck.append(card)

    def shuffle(self):
        random.shuffle(self.cardDeck)

    def add_card(self):
        return self.cardDeck.pop(0)


class Poker:
    def __init__(self, numPlayers):
        self.cardDeck = cardDeck()
        self.cardDeck.shuffle()
        self.hand = []
        numCards = 5

        for i in range(numPlayers):
            hand = []
            for j in range(numCards):
                hand.append(self.cardDeck.add_card())
            self.hand.append(hand)

    def printPlayerHand(self, index):
            orderedHand = sorted(self.hand[index])
            print("Player " + str(index + 1) + "'s hand", end=": ")

            for card in orderedHand:
                print(card, end=" ")
            print()

    def isStraightFlush(self, index):
        orderedHand = sorted(self.hand[index])
        straightFlush = True
        Cardrank = orderedHand[0].rank
        Cardsuit = orderedHand[0].suit
        for card in orderedHand:
            if card.rank != Cardrank or card.suit != Cardsuit:
                straightFlush = False
                self.isFourOfAKind(orderedHand)
                break
            else:
                Cardrank = Cardrank + 1
        if straightFlush:
            print("Straight Flush")

    def isFourOfAKind(self, hand):
        Cardrank = hand[2].rank
        amountCards = 0
        for card in hand:
            if card.rank == Cardrank:
                amountCards = amountCards + 1
        if amountCards == 4:
            print("Four of a kind")
        else:
            self.isFullHouse(hand)

    def isFullHouse(self, hand):
        ranks = []
        for card in hand:
            ranks.append(card.rank)
        leftSideRank = hand[0].rank
        rightSideRank = hand[len(hand)-1].rank
        amountOfLeftSideRanks = ranks.count(leftSideRank)
        amountOfRightSideRanks = ranks.count(rightSideRank)
        if amountOfLeftSideRanks == 3 and amountOfRightSideRanks == 2 or amountOfLeftSideRanks == 2 and amountOfRightSideRanks == 3:
            print("Full House")
        else:    
            self.isFlush(hand)

    def isFlush(self, hand):
        Flush = True
        Cardsuit = hand[0].suit
        for card in hand:
            if card.suit != Cardsuit:
                Flush = False
                self.isStraight(hand)
                break
        if Flush:
            print("Flush")

    def isStraight(self, hand):
        Straight = True
        Cardrank = hand[0].rank
        for card in hand:
            if card.rank != Cardrank:
                Straight = False
                self.isThreeOfAKind(hand)
                break
            else:
                Cardrank = Cardrank + 1
        if Straight:
            print("Straight")

    def isThreeOfAKind(self, hand):
        Cardrank = hand[2].rank
        amountCards = 0
        for card in hand:
            if card.rank == Cardrank:
                amountCards = amountCards + 1
        if amountCards == 3:
            print("Three of a kind")
        else:
            self.isTwoPairs(hand)

    def isTwoPairs(self, hand):
        FirstRank = hand[1].rank
        SecondRank = hand[3].rank
        ranks = []
        for card in hand:
            ranks.append(card.rank)
        if ranks.count(FirstRank) == 2 and ranks.count(SecondRank) == 2:
            print("Two Pairs")
        else:
            self.isOnePair(hand)

    def isOnePair(self, hand):
        counting = []
        ranks = []
        for card in hand:
            ranks.append(card.rank)
        for rank in ranks:
            rankings = ranks.count(rank)
            counting.append(rankings)
        if counting.count(2) == 2:
            print("One pair")
        else:
            self.isHighCard(hand)

    def isHighCard(self, hand):
        print("High Card")

numPlayers = int(input("Enter the amount of players: "))
startRound = Poker(numPlayers)
print("-----------------------------")
for i in range(0, numPlayers):
    startRound.printPlayerHand(i)
    startRound.isStraightFlush(i)
    print()
