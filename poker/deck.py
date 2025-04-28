from treys import Deck as TreysDeck

class Deck:
    def __init__(self):
        self.deck = TreysDeck()

    def draw(self, num=1):
        return [self.deck.draw(1)[0] for _ in range(num)]

    def remove_cards(self, cards):
        for card in cards:
            if card in self.deck.cards:
                self.deck.cards.remove(card)
