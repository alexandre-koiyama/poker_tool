from treys import Evaluator as TreysEvaluator

class Evaluator:
    def __init__(self):
        self.evaluator = TreysEvaluator()

    def evaluate(self, hand, board):
        return self.evaluator.evaluate(hand, board)
