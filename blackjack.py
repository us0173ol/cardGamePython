
from dealer import *
from player import Player
from deck import *
from card import *
# from game_logic import *

def main():

    playerName = input("What is your name? ")
    dealerName = input("What is your dealers name? ")
    player = Player(playerName)
    dealer = Dealer(dealerName)
    deck = Deck()
    deck.shuffle()
    player.draw(deck)
    dealer.draw(deck)
    player.draw(deck)
    dealer.draw(deck)

    print(player.name, "has: ")
    player.showHand()

    print(dealer.name, "shows: ")
    dealer.showOneCard()

    print(player.name, "has a total of: ", player.getValue())

    t = True
    while player.getValue() < int(21) and t == True:
        hit = str(input("Hit (h) or Stay (s)? " ))
        if hit == str("h"):
            player.draw(deck)
            print(player.name, "has: ")
            player.showHand()
            print(player.name, "has a total of: ", player.getValue())

            if player.getValue() > int(21):
                print ("You went over, Dealer wins!!")
                d = False
                break
            if player.getValue() == int(21):
                print("Blackjack!")
                t = False
                d = True
        elif hit == str("s"):
            t = False
            d = True
            print("You have decided to stay. ")
            print(dealer.name, "has: ")
            dealer.showHand()
            print(dealer.name, "has a total of: ", dealer.getValue())


    while d == True:

        if player.getValue() == int(21) and dealer.getValue() < int(21):
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
            print("You win!")
            break




if __name__ == '__main__':
    main()
