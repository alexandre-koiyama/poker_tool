from deck import Deck
from evaluator import Evaluator
from card import Card
from hand import Hand
import random


class PokerSimulator:
    def __init__(self, num_players=9, num_simulations=15000):
        self.num_players = num_players
        self.num_simulations = num_simulations
        self.evaluator = Evaluator()

    def calculate_win_probability(self, my_cards, flop_cards=None, turn_card=None, river_card=None, num_players=None):
        my_hand = [Card.create(c) for c in my_cards]
        known_board = []
        if flop_cards:
            known_board += [Card.create(c) for c in flop_cards]
        if turn_card:
            known_board.append(Card.create(turn_card))
        if river_card:
            known_board.append(Card.create(river_card))

        wins = 0
        players = num_players if num_players else self.num_players  # 👈 override if provided

        for _ in range(self.num_simulations):
            deck = Deck()
            deck.remove_cards(my_hand + known_board)

            opponents = []
            for _ in range(players - 1): 
                opponents.append([deck.draw()[0], deck.draw()[0]])

            board = known_board.copy()
            while len(board) < 5:
                board.append(deck.draw()[0])

            my_score = self.evaluator.evaluate(my_hand, board)
            opponents_scores = [self.evaluator.evaluate(opp, board) for opp in opponents]

            if all(my_score <= opp_score for opp_score in opponents_scores):
                wins += 1

        return wins / self.num_simulations
