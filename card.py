

class Card(object):
#card class to creat a card that I can get values from
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
#show method to print the cards rank and suit
    def show(self):
        print ("{} of {} ".format(self.rank, self.suit))
#get the card value for comparison
    def cardValue(self):
        return self.value
