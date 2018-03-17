from card import *
from deck import *


class Player(object):
#player class with player attributes
    def __init__(self, name):
        self.name = name
        self.hand = []
#draw or get dealt from the deck and add to players hand
    def draw(self, deck):
        draw = self.hand.append(deck.draw())
        return draw
#see the cards in the players hand
    def showHand(self):
        for card in self.hand:
            card.show()
#extract the value of the card so they can be added together for
#comparison with the dealers hand
    def getValue(self):
        handvalue = 0
        for cards in self.hand:
            handvalue += int(cards.value)
        return handvalue

        
