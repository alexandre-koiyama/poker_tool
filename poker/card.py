from treys import Card as TreysCard

class Card:
    @staticmethod
    def create(card_str):
        return TreysCard.new(card_str.lower().replace('10', 'T'))
