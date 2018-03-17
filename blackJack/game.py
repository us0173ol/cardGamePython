import dealer
from dealer import *
import player
from player import *
import deck
from deck import *
import card
from card import *
import blackjack
from blackjack import *
#this logic is designed for one on one play, but determines a winner based on the
#value of their cards.  (d)etermines was the meaning of the variable d. The highest
#hand wins without going over 21.  The dealer has to hit if the have less than 17.

def determine_a_winner(players, dealer, deck, d):


    for player in players:

        while d == True:

            if player.getValue() == 21 and dealer.getValue() < 21:
                dealer.draw(deck)
                print(dealer.name, "has: ")
                dealer.showHand()
                print(dealer.name, "has a total of: ", dealer.getValue())
            elif dealer.getValue() > player.getValue() and dealer.getValue() > int(16) and dealer.getValue() < int(22):
                print("Dealer wins!!")
                break
            elif dealer.getValue() == player.getValue() and dealer.getValue() > int(16) and dealer.getValue() < int(22):
                print("Push!")
                break
            elif dealer.getValue() < int(17):
                dealer.draw(deck)
                print(dealer.name, "has: ")
                dealer.showHand()
                print(dealer.name, "has a total of: ", dealer.getValue())
            else:
                print("{} wins!".format(player.name))
                break
#creates a dealer object
def create_dealer():
    dealer = Dealer("Dealer")
    return dealer
#creates a player object
def create_players():
    players = []
    numOfPlayers = blackjack.number_of_players("How many human players?", 1)
    namesOfPlayers = blackjack.getNames(numOfPlayers, 'Player')
    players = [ Player(name) for name in namesOfPlayers]
    return players
#creates a deck object, which is a deck of cards with suits, ranks, and values
def create_deck():
    deck = Deck()
    deck.shuffle()
    return deck
#deals 2 cards to each player and 2 to the dealer, this is the start of the game
def deal(players, dealer, deck):
    for player in players:
        player.draw(deck)
        player.draw(deck)

    dealer.draw(deck)
    dealer.draw(deck)
#once cards have been dealt, show both cards for the user and one for the dealer
def playGame(players, dealer, deck):
    for player in players:
        print(player.name, "has: ")
        player.showHand()

        print(dealer.name, "shows: ")
        dealer.showOneCard()

        print(player.name, "has a total of: ", player.getValue())

        t = True
    #this is where the user decides if they want to hit(add another card) or stay
    #with what theyve got.  This decision is made while only seeing one dealer card
        while player.getValue() < int(21) and t == True:
            hit = str(input("Hit (h) or Stay (s) {}? ".format(player.name)))
            if hit == str("h"):
                player.draw(deck) #hit
                print(player.name, "has: ")
                player.showHand() #cards in hand
                print(player.name, "has a total of: ", player.getValue()) #value of hand
                #if the player goes over 21 they lose immediately
                if player.getValue() > int(21):
                    print ("You went over, Dealer wins!!")
                    d = False
                    break
                #if the player gets 21 the dealer still has a chance to match(push)
                if player.getValue() == int(21):
                    print("Blackjack!")
                    t = False
                    d = True
                    return d #return d as true to move in to the determine winner function
            elif hit == str("s"):
                t = False
                d = True
                print("You have decided to stay. ")
                print(dealer.name, "has: ")
                dealer.showHand()
                print(dealer.name, "has a total of: ", dealer.getValue())
                return d



def main():

    dealer = create_dealer()
    players = create_players()
    deck = create_deck()
    deal(players, dealer, deck)
    d = playGame(players, dealer, deck)
    determine_a_winner(players, dealer, deck, d)

if __name__ == '__main__':
    main()
