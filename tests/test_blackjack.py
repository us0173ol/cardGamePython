
import unittest
from unittest.mock import patch, MagicMock
from player import *
from deck import *
from card import *
from blackjack import *


class TestBlackjack(unittest.TestCase):

    @patch('builtins.print')
    def test_determine_a_winner(self, mock_print):
        testdeck = Deck()
        testdeck.shuffle()

        testPlayers = []
        player = Player('testMike')
        testPlayers.append(player)
        player.getValue = 20

        testdealer = Dealer('testDealer')
        testdealer.getValue = 19

        game.determine_a_winner(testPlayers, dealer,testdeck, d=True)

        call_args = mock_print.call_args_list

        mock_print.assert_any_call('testDealer has a totoal of: 19')
        mock_print.assert_any_call('testMike wins!')
