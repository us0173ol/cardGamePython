
from dealer import *
from player import *
from deck import *
from card import *

class Game():


     # def setUpGame():

        player = Player("Mike")
        dealer = Dealer("Dealer")
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

        print(player.name, "has a total of:  ", player.getValue())


    # def playGame():
        #boolean was the only way I could think of to control the loops
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
                    break
                if player.getValue() == int(21):
                    print("Blackjack!")
                    t = False
            elif hit == str("s"):
                t = False
                print("You have decided to stay. ")
                print(dealer.name, "has: ")
                dealer.showHand()
                print(dealer.name, "has a total of: ", dealer.getValue())
        

    # def determine_winner():
        while True:
            if dealer.getValue() == player.getValue() and dealer.getValue() > int(16):
                print("Draw!")
                break
            elif dealer.getValue() == player.getValue() and dealer.getValue() < int(17):
                dealer.draw(deck)
                print(dealer.name, "has: ")
                dealer.showHand()
                print(dealer.name, "has a total of: ", dealer.getValue())
            elif dealer.getValue() > player.getValue() and dealer.getValue() < int(22):
                print("Dealer wins!!")
                break
            elif dealer.getValue() < int(17):
                dealer.draw(deck)
                print(dealer.name, "has: ")
                dealer.showHand()
                print(dealer.name, "has a total of: ", dealer.getValue())
            else:
                print("You win!")
                break

def main():

    Game()

if __name__ == '__main__':
    main()
