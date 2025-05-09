import streamlit as st
from simulator import PokerSimulator

# Initialize simulator
simulator = PokerSimulator()

# Card options
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits_symbols = {'h': '♥️', 'd': '♦️', 'c': '♣️', 's': '♠️'}
suits = list(suits_symbols.keys())
symbols = list(suits_symbols.values())

st.title("♠️ Poker Win Probability Calculator")
st.caption("By your assistant 🚀")

#sessions
if 'my_cards' not in st.session_state or st.button('Start New Game'):
    st.session_state.clear()
    st.session_state.my_cards = []
    st.session_state.flop = []
    st.session_state.turn = None
    st.session_state.river = None
    st.session_state.players_preflop = 9
    st.session_state.players_flop = 9
    st.session_state.players_turn = 9
    st.session_state.players_river = 9
    st.session_state.step = 'preflop'
    st.session_state.preflop_probability = None
    st.session_state.flop_probability = None
    st.session_state.turn_probability = None
    st.session_state.river_probability = None
    st.session_state.selected_card1 = None
    st.session_state.selected_suit1 = None
    st.session_state.selected_card2 = None
    st.session_state.selected_suit2 = None
    st.session_state.calc_preflop = None
    st.session_state.calc_flop = None
    st.session_state.calc_turn = None

options_level = ["very low", "low", "medium", "high", "very high"]

# Step 1: Select Hole Cards
st.header("Select Your Hand Cards")

col_hand1_preflop, col_hand2_preflop, col_num_player_preflop, col_calc_preflop = st.columns(4)

# Hand card 1 selection
with col_hand1_preflop:
    select_num1 = st.pills("Card 1", ranks, selection_mode='single', key="select_num1")
    st.session_state.selected_card1 = select_num1
    select_suit1 = st.pills("Suit 1", symbols, selection_mode='single', key="select_suit1")
    if select_suit1 == '♠️':
        st.session_state.selected_suit1 = 's'
    elif select_suit1 == '♣️':
        st.session_state.selected_suit1 = 'c'
    elif select_suit1 == '♦️':
        st.session_state.selected_suit1 = 'd'
    elif select_suit1 == '♥️':
        st.session_state.selected_suit1 = 'h'

# Hand card 2 selection
with col_hand2_preflop:
    select_num2 = st.pills("Card 2", ranks, selection_mode='single', key="select_num2")
    st.session_state.selected_card2 = select_num2
        
    select_suit2 = st.pills("Suit 2", symbols, selection_mode='single', key="select_suit2")
    if select_suit2 == '♠️':
        st.session_state.selected_suit2 = 's'
    elif select_suit2 == '♣️':
        st.session_state.selected_suit2 = 'c'
    elif select_suit2 == '♦️':
        st.session_state.selected_suit2 = 'd'
    elif select_suit2 == '♥️':
        st.session_state.selected_suit2 = 'h'

card1 = st.session_state.selected_card1 + st.session_state.selected_suit1 if st.session_state.selected_card1 and st.session_state.selected_suit1 else None
card2 = st.session_state.selected_card2 + st.session_state.selected_suit2 if st.session_state.selected_card2 and st.session_state.selected_suit2 else None

with col_num_player_preflop:
    st.write("Players Pre-Flop")
    st.session_state.players_preflop = st.slider("Including you", 2, 9, st.session_state.players_preflop, key="payers_preflop")
    if card1 and card2 and card1 != card2:
        st.session_state.my_cards = [card1, card2]
        st.info(f"HAND {st.session_state.selected_card1}{suits_symbols[st.session_state.selected_suit1]} "
                f"{st.session_state.selected_card2}{suits_symbols[st.session_state.selected_suit2]}")
    else:
        st.warning("Please select both hole cards first.")

#  Preflop Calculation
with col_calc_preflop:
    st.write("Level: Pre-Flop")
    selection_level = st.pills("Level", options_level, selection_mode="single", key="selection_level")

    calc_preflop = st.button("Pre-Flop Win Probability",  type='secondary', use_container_width=True)
    if calc_preflop:
        st.session_state.calc_preflop = True
        if len(st.session_state.my_cards) == 2:
            with st.spinner('Calculating...', show_time=True):
                prob_preflop = simulator.calculate_win_probability(
                    my_cards=st.session_state.my_cards,
                    flop_cards=None,
                    turn_card=None,
                    river_card=None,
                    num_players=st.session_state.players_preflop,
                    tier=selection_level
                )
            st.session_state.preflop_probability = prob_preflop
            st.session_state.step = 'flop'
        else:
            st.warning("Please select both hole cards first.")
    st.write(" ")
    if st.session_state.preflop_probability:
        st.success(f"Pre-flop Win Probability: {st.session_state.preflop_probability:.2%}")
    
# Step 4: FLOP
if st.session_state.calc_preflop:
    st.header("Flop Cards")

    col_card1_flop, col_card2_flop, col_card3_flop, col_num_player_flop, col_calc_flop = st.columns(5)

    with col_card1_flop:
        st.session_state.selected_card3 = st.pills("Card 3", ranks, selection_mode='single', key="select_num3")
        st.session_state.selected_suit3 = st.pills("Suit 3", symbols, selection_mode='single', key="select_suit3")
        if st.session_state.selected_suit3 == '♠️':
            st.session_state.selected_suit3 = 's'
        elif st.session_state.selected_suit3 == '♣️':
            st.session_state.selected_suit3 = 'c'
        elif st.session_state.selected_suit3 == '♦️':
            st.session_state.selected_suit3 = 'd'
        elif st.session_state.selected_suit3 == '♥️':
            st.session_state.selected_suit3 = 'h'

    with col_card2_flop:
        st.session_state.selected_card4 = st.pills("Card 4", ranks, selection_mode='single', key="select_num4")
        st.session_state.selected_suit4 = st.pills("Suit 4", symbols, selection_mode='single', key="select_suit4")
        if st.session_state.selected_suit4 == '♠️':
            st.session_state.selected_suit4 = 's'
        elif st.session_state.selected_suit4 == '♣️':
            st.session_state.selected_suit4 = 'c'
        elif st.session_state.selected_suit4 == '♦️':
            st.session_state.selected_suit4 = 'd'
        elif st.session_state.selected_suit4 == '♥️':
            st.session_state.selected_suit4 = 'h'

    with col_card3_flop:
        st.session_state.selected_card5 = st.pills("Card 5", ranks, selection_mode='single', key="select_num5")
        st.session_state.selected_suit5 = st.pills("Suit 5", symbols, selection_mode='single', key="select_suit5")
        if st.session_state.selected_suit5 == '♠️':
            st.session_state.selected_suit5 = 's'
        elif st.session_state.selected_suit5 == '♣️':
            st.session_state.selected_suit5 = 'c'
        elif st.session_state.selected_suit5 == '♦️':
            st.session_state.selected_suit5 = 'd'
        elif st.session_state.selected_suit5 == '♥️':
            st.session_state.selected_suit5 = 'h'

    #update number of players
    with col_num_player_flop:
        st.write("Players in Flop")
        st.session_state.players_flop = st.slider("Including you", 2, st.session_state.players_preflop, st.session_state.players_preflop, key="payers_flop")
        st.write(" ")
        if st.session_state.selected_card3 and st.session_state.selected_card4 and st.session_state.selected_card5:
            st.info(f"HAND {st.session_state.selected_card1}{suits_symbols[st.session_state.selected_suit1]} "
                    f"{st.session_state.selected_card2}{suits_symbols[st.session_state.selected_suit2]}")
            st.info(f"FLOP CARDS {st.session_state.selected_card3}{suits_symbols[st.session_state.selected_suit3]} "
                    f"{st.session_state.selected_card4}{suits_symbols[st.session_state.selected_suit4]} "
                    f"{st.session_state.selected_card5}{suits_symbols[st.session_state.selected_suit5]}")

    with col_calc_flop:
        st.write("Level: Flop")
        selection_level_flop = st.pills("Level", options_level, selection_mode="single", key="selection_level_flop")
        calc_flop = st.button('Flop Win Probability')
        if calc_flop:
            st.session_state.calc_flop = True
            if len(st.session_state.my_cards) == 2:
                with st.spinner('Calculating...', show_time=True):
                    prob_flop = simulator.calculate_win_probability(
                        my_cards=st.session_state.my_cards,
                        flop_cards=[st.session_state.selected_card3+st.session_state.selected_suit3,
                                    st.session_state.selected_card4+st.session_state.selected_suit4,
                                    st.session_state.selected_card5+st.session_state.selected_suit5],
                        turn_card=None,
                        river_card=None,
                        num_players=st.session_state.players_flop,
                        tier=selection_level_flop
                    )
                st.session_state.flop_probability = prob_flop
                st.session_state.step = 'turn'
            else:
                st.warning("Please select both hole cards first.")

        if st.session_state.flop_probability:
                st.success(f"Flop Win Probability: {st.session_state.flop_probability:.2%}")

# Step 5: TURN
if st.session_state.calc_flop:
    st.header("Turn Card")

    col_card1_turn, col_num_player_turn, col_calc_turn = st.columns(3)

    with col_card1_turn:
        st.session_state.selected_card6 = st.pills("Card 6", ranks, selection_mode='single', key="select_num6")
        st.session_state.selected_suit6 = st.pills("Suit 6", symbols, selection_mode='single', key="select_suit6")
        if st.session_state.selected_suit6 == '♠️':
            st.session_state.selected_suit6 = 's'
        elif st.session_state.selected_suit6 == '♣️':
            st.session_state.selected_suit6 = 'c'
        elif st.session_state.selected_suit6 == '♦️':
            st.session_state.selected_suit6 = 'd'
        elif st.session_state.selected_suit6 == '♥️':
            st.session_state.selected_suit6 = 'h'

    #update number of players
    with col_num_player_turn:
        st.write("Number of Players in Turn")
        st.session_state.players_turn = st.slider("Including you", 2, st.session_state.players_flop, st.session_state.players_flop, key="payers_turn")

        if st.session_state.selected_card3 and st.session_state.selected_card4 and st.session_state.selected_card5 and st.session_state.selected_card6:
            st.info(f"HAND {st.session_state.selected_card1}{suits_symbols[st.session_state.selected_suit1]} "
                    f"{st.session_state.selected_card2}{suits_symbols[st.session_state.selected_suit2]}")
            st.info(f"FLOP CARDS {st.session_state.selected_card3}{suits_symbols[st.session_state.selected_suit3]} "
                    f"{st.session_state.selected_card4}{suits_symbols[st.session_state.selected_suit4]} "
                    f"{st.session_state.selected_card5}{suits_symbols[st.session_state.selected_suit5]}"
                    f"{st.session_state.selected_card6}{suits_symbols[st.session_state.selected_suit6]}")

    with col_calc_turn:
        st.write("Level: Turn")
        selection_level_turn= st.pills("Level", options_level, selection_mode="single", key="selection_level_turn")

        calc_turn = st.button('Calculate Turn Win Probability')
        if calc_turn:
            st.session_state.calc_turn = True
            if len(st.session_state.my_cards) == 2:
                with st.spinner('Calculating...', show_time=True):
                    prob_turn = simulator.calculate_win_probability(
                        my_cards=st.session_state.my_cards,
                        flop_cards=[st.session_state.selected_card3+st.session_state.selected_suit3,
                                    st.session_state.selected_card4+st.session_state.selected_suit4,
                                    st.session_state.selected_card5+st.session_state.selected_suit5],
                        turn_card=st.session_state.selected_card6+st.session_state.selected_suit6,
                        river_card=None,
                        num_players=st.session_state.players_turn,
                        tier=selection_level_turn
                    )
                st.session_state.turn_probability = prob_turn
                st.session_state.step = 'river'
            else:
                st.warning("Please select both hole cards first.")

        if st.session_state.turn_probability:
                st.success(f"Turn Win Probability: {st.session_state.turn_probability:.2%}")

# Step 6: RIVER
if st.session_state.calc_turn:
    st.header("River Card")

    col_card1_river, col_num_player_river, col_calc_river = st.columns(3)

    with col_card1_river:
        st.session_state.selected_card7 = st.pills("Card 7", ranks, selection_mode='single', key="select_num7")
        st.session_state.selected_suit7 = st.pills("Suit 7", symbols, selection_mode='single', key="select_suit7")
        if st.session_state.selected_suit7 == '♠️':
            st.session_state.selected_suit7 = 's'
        elif st.session_state.selected_suit7 == '♣️':
            st.session_state.selected_suit7 = 'c'
        elif st.session_state.selected_suit7 == '♦️':
            st.session_state.selected_suit7 = 'd'
        elif st.session_state.selected_suit7 == '♥️':
            st.session_state.selected_suit7 = 'h'

    #update number of players
    with col_num_player_river:
        st.write("Number of Players in River")
        if st.session_state.players_turn ==2:
            st.session_state.players_river = st.session_state.players_turn  
            st.write("Including you")
            st.warning("2 players")
        else:
            st.session_state.players_river = st.slider("Including you", 2, st.session_state.players_turn, st.session_state.players_turn, key="payers_river")
        if st.session_state.selected_card3 and st.session_state.selected_card4 and st.session_state.selected_card5 and st.session_state.selected_card6 and st.session_state.selected_card7:
            st.info(f"HAND {st.session_state.selected_card1}{suits_symbols[st.session_state.selected_suit1]} "
                    f"{st.session_state.selected_card2}{suits_symbols[st.session_state.selected_suit2]}")
            st.info(f"FLOP CARDS {st.session_state.selected_card3}{suits_symbols[st.session_state.selected_suit3]} "
                    f"{st.session_state.selected_card4}{suits_symbols[st.session_state.selected_suit4]} "
                    f"{st.session_state.selected_card5}{suits_symbols[st.session_state.selected_suit5]}"
                    f"{st.session_state.selected_card6}{suits_symbols[st.session_state.selected_suit6]}"
                    f"{st.session_state.selected_card7}{suits_symbols[st.session_state.selected_suit7]}")

    with col_calc_river:
        st.write("Level: River")
        selection_level_river = st.pills("Level", options_level, selection_mode="single", key="selection_level_river")

        if st.button('Calculate River Win Probability'):
            if len(st.session_state.my_cards) == 2:
                with st.spinner('Calculating...', show_time=True):
                    prob_river = simulator.calculate_win_probability(
                        my_cards=st.session_state.my_cards,
                        flop_cards=[st.session_state.selected_card3+st.session_state.selected_suit3,
                                    st.session_state.selected_card4+st.session_state.selected_suit4,
                                    st.session_state.selected_card5+st.session_state.selected_suit5],
                        turn_card=st.session_state.selected_card6+st.session_state.selected_suit6,
                        river_card=st.session_state.selected_card7+st.session_state.selected_suit7,
                        num_players=st.session_state.players_river,
                        tier=selection_level_river
                    )
                st.session_state.river_probability = prob_river
                st.session_state.step = 'showdown'
            else:
                st.warning("Please select both hole cards first.")

        if st.session_state.river_probability:
                st.success(f"River Win Probability: {st.session_state.river_probability:.2%}")

#Next steps
# - show probability of winning hands for flop, turn and river (example for flop, hand =  9h,8h flop = 2h,5h,6c) - 50% of winning flush and 30% of winning straight 
