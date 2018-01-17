import random

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

class Player (object):
#player class with player attributes
    def __init__(self, name):
        self.name = name
        self.hand = []
#draw or get dealt from the deck and add to players hand
    def draw(self, deck):
        self.hand.append(deck.draw())
        return self
#see the cards in the players hand
    def showHand(self):
        for card in self.hand:
            card.show()
            # print(self.name, "has: "+ str(card.show()))
#extract the value of the card so they can be added together for
#comparison with the dealers hand
    def getValue (self):
        self.playerHand = []
        for cards in self.hand:
            self.playerHand.append(int(cards.value))
#after the values have been added to a list, add them together
        print(sum(self.playerHand))
        return sum(self.playerHand)

class Dealer (object):
#dealer class to essentially mirror the player class
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self
#still figuring out how to show only one card, not just the value
#and in a user friendly manner, trying to not show the location of
#the object in output
    def showHand(self):
        # self.dH = []
        for card in self.hand:
             card.show()
        #     self.dH.append(str(card.show))
        # print(self.dH[1])
#get value of dealers hand
    def getValue(self):
        self.dealerHand = []
        for cards in self.hand:
            self.dealerHand.append(int(cards.value))

        print(sum(self.dealerHand))
        return sum(self.dealerHand)

# name = input("What is your name? ")
# player = Player(str(name))


#I wasnt sure if I should make this all one class or find a better way
#to split it up.  I tried to keep it simple but it just became more
#complicated the further I got, need to fix way of getting values of
#cards so I dont display the values when comparing them.
class Game():
    player = Player("Mike")
    dealer = Dealer("Dealer")
    deck = Deck()
    deck.shuffle()
    player.draw(deck)
    dealer.draw(deck)
    player.draw(deck)
    dealer.draw(deck)
#I numbered all of my print statements so I could at least follow where
#things were printing out, I dont know how to go step by step in Python
    print(player.name, "has1: ")
    player.showHand()

    print(dealer.name, "shows2: ")
    dealer.showHand()

    print(player.name, "has3:  ")
    player.getValue()
#boolean was the only way I could think of to control the loops
    t = True
    while player.getValue() < int(21) and t == True:
        hit = str(input("Hit (h) or Stay (s)? " ))
        if hit == str("h"):
            player.draw(deck)
            print(player.name, "has4: ")
            player.showHand()

            print(player.name, "has5: ")
            player.getValue()

            if player.getValue() > int(21):
                print ("You went over, Dealer wins!!")
                break
            if player.getValue() == int(21):
                print("Blackjack!")
                t = False
        elif hit == str("s"):
            t = False
            print("You have decided to stay. ")
            while dealer.getValue() <= player.getValue():
                dealer.draw(deck)
                print(dealer.name, "has6: ")
                dealer.showHand()
                print(dealer.name, "has7: ")
                dealer.getValue()
#one of my main problems is here where I used the get value methods
#from the player and dealer classes to compare values, problem is,
#when I do they print the values when I dont want them to
                if dealer.getValue() == player.getValue():
                    print("Draw!")
                    break
                elif dealer.getValue() > player.getValue() and dealer.getValue() < int(22):
                    print("Dealer wins!!")
                    break
                elif dealer.getValue() < int(17):
                    dealer.draw(deck)
                    print(dealer.name, "has8: ")
                    dealer.showHand()
                    print(dealer.name, "has9: ")
                    dealer.getValue()
                else:
                    print("You win!")
                    break
#TODO add play again?
game = Game()
