import sys
sys.path.append('.')
import unittest
from unittest.mock import patch, MagicMock
# import blackJack

# from blackJack
import player, card, deck, blackjack, game, dealer
from deck import *
from card import *
from blackjack import *


class TestBlackjack(unittest.TestCase):


    def test_int(self):
        print('Here goes the int function:', int(3))

    @patch('builtins.print')
    def test_determine_a_winner(self, mock_print):


        testdeck = Deck()
        testdeck.shuffle()

        testPlayers = []

        # Watch your names. You are assiging the player module to be a new Player() object
        # which is causing a weird test failure.

        humanPlayer = player.Player('testMike')
        testPlayers.append(humanPlayer)
        humanPlayer.getValue = 20  #  problem: is this the right thing to do to set the player's value?

        testdealer = dealer.Dealer('testDealer')
        estdealer.getValue = 19  # Same here  - find another way to force the player to have a certain value

        # Same here - dealer is a module, not a dealer object
        game.determine_a_winner(testPlayers, testdealer, testdeck, d=True)  # getting int object is not callable - related to the player.setvalue = 20 calls above. Review and revise these

        call_args = mock_print.call_args_list

        mock_print.assert_any_call('testDealer has a totoal of: 19')
        mock_print.assert_any_call('testMike wins!')
