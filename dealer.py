from card import *
from deck import *


class Dealer (object):
#dealer class to essentially mirror the player class
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        draw = self.hand.append(deck.draw())
        return draw
#still figuring out how to show only one card, not just the value
#and in a user friendly manner, trying to not show the location of
#the object in output
    def showOneCard(self):
        for card in self.hand:
            if card is self.hand[0]:
                card.show()
                
    def showHand(self):
        for card in self.hand:
            card.show()

    def getValue(self):
        self.dealerHand = []
        handvalue = 0
        for cards in self.hand:
            handvalue += int(cards.value)
        return handvalue
