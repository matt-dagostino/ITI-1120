# ------------------------------------------------
#              Assignment 4 - Poker
#           Matteo Dagostino 300287930
#               mdago035@uottawa.ca
# ------------------------------------------------

# Importing python libraries
import random
import math
import string
import os
os.system(('cls' if os.name == 'nt' else 'clear'))  # Clears the console

class Card: # Creating the Card class which will define which cards are available and their suits
    presetRank = [
        # Available Ranks
        1, # Ace
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10, # Ten
        11, # Jack
        12, # Queen
        13, # King
        ]

    presetSuit = ["D", "C", "S", "H"] # Diamonds, Clubs, Spades, Hearts

    def __init__(self, rank, suit): # Initialize variables (setting their self values equal to their suits and ranks)
        self.rank = rank
        self.suit = suit

    def __eq__(self, compared):  # Equal to (comparing)
        return self.rank == compared.rank

    def __ne__(self, compared):  # Not Equal to (comparing)
        return self.rank != compared.rank

    def __ge__(self, compared):  # Greater than or equal (comparing)
        return self.rank >= compared.rank

    def __le__(self, compared):  # Less than or equal (comparing)
        return self.rank <= compared.rank

    def __gt__(self, compared):  # Greater than (comparing)
        return self.rank > compared.rank

    def __lt__(self, compared):  # Less than (comparing)
        return self.rank < compared.rank

    def __str__(self): # Returning string representation of the rank objects (converting numbers to T, J, Q, K and A)
        # Converting 10 to T
        if self.rank == 10:
            rank = "T"
        # Converting 11 to J
        elif self.rank == 11:
            rank = "J"
        # Converting 12 to Q
        elif self.rank == 12:
            rank = "Q"
        # Converting 13 to K
        elif self.rank == 13:
            rank = "K"
        # Converting 1 to A
        elif self.rank == 1:
            rank = "A"
        # If the number doesnt need to be converted to a letter, then
        else:
            rank = self.rank
        #Return the card's rank and suit
        return str(rank) + self.suit

class cardDeck: # Creating a class for the deck of cards that will be used in the game
    def __init__(self): # Creating the deck of cards
        self.cardDeck = [] # Start with empty deck
        for suit in Card.presetSuit: # For every suit
            for rank in Card.presetRank: # For every rank
                card = Card(rank, suit) # Add rank and suit to create card
                self.cardDeck.append(card) # Add card to deck of cards

    def shuffle(self):
        # Function that will randomly shuffle the deck of cards using the 'random' library
        random.shuffle(self.cardDeck)

    def add_card(self):
        # Removing the first card from the deck and returning the value of that card
        return self.cardDeck.pop(0)

class PokerGame: # Creating the main Poker class
    def __init__(self, numPlayers): 
        # Initializing the deck or cards
        self.cardDeck = cardDeck()
        # Shuffling the cards
        self.cardDeck.shuffle()
        self.hand = [] # Creating the player's hand
        numCards = 5 # Number of cards per player (change if you want player to receive more/less cards)

        for i in range(numPlayers): # Repeat for the amount of players that are in the game
            hand = [] # Start with empty player hand
            for j in range(numCards): # Repeat for the amount of cards each player will have
                hand.append(self.cardDeck.add_card()) # Add a card to their hand
            self.hand.append(hand) # Add the player's hand to their self.hand 

    def add_to_table(self, cardNumber): # Function that will add the top card to the table (receives amount of cards wanted to be on table)
        table = [] # Table starts with no cards on it (empty list)
        for i in range(0, cardNumber): # Repeat for amount of cards wanted to be on table
            table.append(self.cardDeck.add_card()) # Add the top card from the deck to the table
        return table # Return the list of cards on the table

    def printPlayerHand(self, index): # Function that will print a player's hand
            orderedHand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit)
            print("Player " + str(index + 1) + "'s hand", end=": ") # Printing the player's ID (example: Player 1's hand: )

            for card in orderedHand: # For each card in the player's hand
                print(card, end=" ") # Print the card
            print() # Print empty line (pretty output)
    
    def printTable(self, table): # Function that will print the cards on the table (receives the list of cards on table)
            orderedTable = sorted(table) # Sorts the table (smallest card value to highest, regardless of suit)
            print("Cards on table: ")
            for card in orderedTable: # For each card on the table
                print(card, end=" ") # Print the card
            print() # Print empty line (pretty output)

    def isStraightFlush(self, index): # Function to check of hand is straight flush
        orderedHand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit) 
        Cardrank = orderedHand[0].rank # Set the universal card rank to the rank of the first card
        Cardsuit = orderedHand[0].suit # Set the universal card suit to the suit of the first card
        for card in orderedHand:
            if card.rank != Cardrank or card.suit != Cardsuit: # If the rank isnt consecutive and/or the suit is different, then
                return False
            else:
                Cardrank = Cardrank + 1 # Add 1 to the universal card rank (consecutive)
        return True

    def isFourOfAKind(self, index): # Function to check of hand is four of a kind
        hand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit)
        Cardrank = hand[2].rank # Set the universal card rank to the rank of the third card since if it is four of a kind, the set will have the rank of the 3rd card no matter what
        amountCards = 0 # Setting the amount of cards repeated to 0
        for card in hand:
            if card.rank == Cardrank: # If the card has the universal card rank
                amountCards = amountCards + 1 # Add 1 to amount of cards
        if amountCards == 4: # If it is a four of a kind, then
            return True
        else:
            return False

    def isFullHouse(self, index): # Function to check of hand is full house
        hand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit)
        ranks = [] # Will contain the ranks of all cards
        for card in hand:
            # Adding the card rank to the list of ranks
            ranks.append(card.rank)
        A = hand[0].rank # A is the ranks of the cards on the left side of the full house (example: A-A-B-B-B)
        B = hand[len(hand)-1].rank # B is the ranks of the cards on the right side of the full house (example: A-A-B-B-B)
        amountOfA = ranks.count(A) # Count the amount of A's
        amountOfB = ranks.count(B) # Count the amount of B's
        if amountOfA == 3 and amountOfB == 2 or amountOfA == 2 and amountOfB == 3: # If it is a full house, then
            return True
        else:    
            return False

    def isFlush(self, index): # Function to check of hand is flush
        hand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit)
        Cardsuit = hand[0].suit # Set the universal card suit to the suit of the first card
        for card in hand:
            if card.suit != Cardsuit: # If the card's suit is not the same as the first card's suit, then
                return False
        return True

    def isStraight(self, index): # Function to check of hand is straight
        hand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit)
        Cardrank = hand[0].rank # Set the universal card rank to the rank of the first card
        for card in hand:
            if card.rank != Cardrank: # If the rank is not consecutive, then
                return False
            else:
                Cardrank = Cardrank + 1 # Add one to the universal card rank (consecutive)
        return True

    def isThreeOfAKind(self, index): # Function to check of hand is three of a kind
        hand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit)
        Cardrank = hand[2].rank # Set the universal card rank to the rank of the third card (if three of a kind is a True, the rank will be the third card's rank)
        amountCards = 0 # Set the amount of cards in three of a kind set to 0
        for card in hand:
            if card.rank == Cardrank: # If the card's rank is the same as the universal card rank, then
                amountCards = amountCards + 1 # Add 1 to the amount of cards in the three of a kind set
        if amountCards == 3: # If there is a three of a kind in the hand, then
            return True
        else:
            return False

    def isTwoPairs(self, index): # Function to check of hand is two pairs
        hand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit)
        FirstRank = hand[1].rank # Set the first universal rank of the two pair to the second card's rank in the hand
        SecondRank = hand[3].rank # Set the second universal rank of the two pair to the fourth card's rank in the hand
        ranks = [] # Empty list for storing ranks
        for card in hand:
            ranks.append(card.rank) # Store the card's rank in the ranks list
        if ranks.count(FirstRank) == 2 and ranks.count(SecondRank) == 2: # If the hand contains two pairs, then
            return True
        else:
            return False

    def isOnePair(self, index): # Function to check of hand is one pair
        hand = sorted(self.hand[index]) # Sort the hand (smallest card value to highest, regardless of suit)
        counting = [] # Empty list for counting
        ranks = [] # Empty list for storing ranks
        for card in hand:
            ranks.append(card.rank) # Store the card's rank in the ranks list
        for rank in ranks: # For every rank in the hand
            rankings = ranks.count(rank) # Count the amount of each rank (if a rank is repeated)
            counting.append(rankings) # Add the amount of a rank to the counting list
        if counting.count(2) == 2: # If a rank repeats twice, it contains a pair, True
            return True
        else:
            return False

class TexasHoldem(PokerGame): # Create texas hold em class
    def __init__(self):
        super().__init__(numPlayers) # Super the values from PokerGame class



numPlayers = int(input("Enter the amount of players: ")) # Asks the user to enter the amount of players
startRound = PokerGame(numPlayers) # Starts the game

# ------------- Uncomment the 2 lines bellow to add cards to the table --------------------
# amountCards = 2
# CardsOnTable = startRound.add_to_table(amountCards)
# startRound.printTable(CardsOnTable)

# The lines below will print every player's hand aswell as their rank (one pair, two pair... etc)
print("-----------------------------")
for i in range(0, numPlayers):
    startRound.printPlayerHand(i)
    if startRound.isStraightFlush(i):
        print("Straight Flush")
    elif startRound.isFourOfAKind(i):
        print("Four of a kind")
    elif startRound.isFullHouse(i):
        print("Full House")
    elif startRound.isFlush(i):
        print("Flush")
    elif startRound.isStraight(i):
        print("Straight")
    elif startRound.isThreeOfAKind(i):
        print("Three of a kind")
    elif startRound.isTwoPairs(i):
        print("Two pairs")
    elif startRound.isOnePair(i):
        print("One pair")
    else:
        print("High Card")
    print()