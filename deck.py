#Deck of cards and your metods

from random import shuffle

class Card:
#Create a Card object
     
    def __init__ (self, value, suit):
        self.suit = suit
        self.value = value
        
class Deck:
#Create a deck object
    
    def __init__ (self):
        self.cards = []
        self.build()
    #init a deck making cards and build a deck
    
    def build (self):
        self.cards = [Card(value, suit) for value in values for suit in suits]
    #method for create a deck of cards
    
    def show (self):
        for c in range (0, len(self.cards)):
            print (f'{self.cards[c].suit} - {self.cards[c].value}')
    #method for show a deck list
            
    def deckShuffle (self):
        shuffle(self.cards)
    #shuffle this deck
        
    def addJoker (self):
        for c in ('red', 'black'):
            self.cards.append(Card('Joker', c))
    #add two jokers of the deck
        
suits = ('spades', 'hearth', 'diamonds', 'clubs')
values = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
