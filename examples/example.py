from poker.simulator import PokerSimulator

simulator = PokerSimulator(num_players=9, num_simulations=5000)

my_cards = ['As', 'Kd']
flop = ['Ah', '7s', '2c']
turn = '5d'
river = None

prob = simulator.calculate_win_probability(my_cards, flop, turn, river)
print(f"Winning probability: {prob*100:.2f}%")
