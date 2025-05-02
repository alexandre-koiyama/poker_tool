from deck import Deck
from evaluator import Evaluator
from card import Card
from hand import Hand
from hand_tiers import Tiers
import random
import time

class PokerSimulator:
    def __init__(self, num_players=9, num_simulations=5000):
        self.num_players = num_players
        self.num_simulations = num_simulations
        self.evaluator = Evaluator()

    def calculate_win_probability(self, my_cards, flop_cards=None, turn_card=None, river_card=None, num_players=None, tier='very low'):
        my_hand = [Card.create(c) for c in my_cards]
        known_board = []
        if flop_cards:
            known_board += [Card.create(c) for c in flop_cards]
        if turn_card:
            known_board.append(Card.create(turn_card))
        if river_card:
            known_board.append(Card.create(river_card))

        Tier = Tiers()

        wins = 0
        players = num_players if num_players else self.num_players  

        very_low_tier = Tier.get_very_low_group()
        low_tier = Tier.get_low_group()
        medium_tier = Tier.get_medium_group()
        high_tier = Tier.get_high_group()
        very_high_tier = Tier.get_very_high_group()
       
        if tier == 'very low':
            tier_cards = very_low_tier
        elif tier == 'low':
            tier_cards = low_tier
        elif tier == 'medium':
            tier_cards = medium_tier
        elif tier == 'high':
            tier_cards = high_tier
        elif tier == 'very high':
            tier_cards = very_high_tier

        if tier != None:
            tier_card_values = [sorted([Card.create(pair_t[0]), Card.create(pair_t[1])]) for pair_t in tier_cards] 

        init_deck = Deck()
        init_deck.remove_cards(my_hand + known_board)
        all_pair_combinations = init_deck.get_allcombination_2cards()
        
        for _ in range(self.num_simulations):
            deck = Deck()
            deck.remove_cards(my_hand + known_board)
            opponents = []
            n_opponents = 0

            while n_opponents <= players - 1:
                opponets_hand = random.choice(all_pair_combinations)
                if opponets_hand in tier_card_values:
                    deck.remove_cards(opponets_hand)
                    opponents.append(opponets_hand)
                    n_opponents += 1
        
            board = known_board.copy()
            while len(board) < 5:
                board.append(deck.draw()[0])

            my_score = self.evaluator.evaluate(my_hand, board)
            opponents_scores = [self.evaluator.evaluate(opp, board) for opp in opponents]

            if all(my_score <= opp_score for opp_score in opponents_scores):
                wins += 1
    
        
        return wins / self.num_simulations