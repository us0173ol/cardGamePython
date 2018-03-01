from card import *
from deck import *


class Dealer (object):
#dealer class to essentially mirror the player class
    def __init__(self, name):
        self.hand = []
        self.name = name
#draw adds a card from the deck to the dealers hand of cards
    def draw(self, deck):
        draw = self.hand.append(deck.draw())
        return draw
#shows only one card in dealers hand
    def showOneCard(self):
        for card in self.hand:
            if card is self.hand[0]:
                card.show()
#shows all cards in dealers hand
    def showHand(self):
        for card in self.hand:
            card.show()
#gets the value of the hand (21 = blackjack)
    def getValue(self):
        self.dealerHand = []
        handvalue = 0
        for cards in self.hand:
            handvalue += int(cards.value)
        return handvalue
