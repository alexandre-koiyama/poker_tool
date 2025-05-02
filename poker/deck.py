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

    def return_cards(self, cards):
        for card in cards:
            if card not in self.deck.cards:
                self.deck.cards.append(card)

    def get_allcombination_2cards(self):
        deck_pairs = []
        for card1 in self.deck.cards:
            for card2 in self.deck.cards:
                if card1 != card2:
                    if sorted([card1, card2]) not in deck_pairs:
                        deck_pairs.append(sorted([card1, card2]))
        return deck_pairs
