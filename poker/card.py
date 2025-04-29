from treys import Card as TCard

class Card:
    @staticmethod
    def create(card_str):
        if len(card_str) == 2 and card_str[0] == '1':
            card_str = 'A' + card_str[1]
        card_str = card_str.replace('10', 'T')
        first_char = card_str[0].upper()
        second_char = card_str[1].lower()
        card_str = f'{first_char}{second_char}'
        return TCard.new(card_str)