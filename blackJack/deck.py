from card import *
import random


class Deck(object):
#deck class to create, shuffle, deal (draw from) and to show the deck if needed
    def __init__(self):
        self.cards = []
        self.create()
#create a deck with suits, proper ranks and values
    def create(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                if value > 1 and value < 11:
                    rank = value
                if value == 1:
                    rank = "Ace"
                    value = 11
                if value == 11:
                    rank = "Jack"
                    value = 10
                if value == 12:
                    rank = "Queen"
                    value = 10
                if value == 13:
                    rank = "King"
                    value = 10
                #add the cards to the card list(Deck)
                self.cards.append(Card(suit, rank, value))
#to check if the cards in the hands are coming out of the deck
    def show(self):
        for card in self.cards:
            card.show()
#shuffle the deck randomly
    def shuffle(self):
        #start at the end of the list of cards, go to zero, decrementing
        for i in range(len(self.cards)-1, 0, -1):
            #pick random element from the list to shuffle
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
#draw method for dealing
    def draw(self):
        return self.cards.pop()
