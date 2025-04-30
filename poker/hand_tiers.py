import json

class Tiers:
    def __init__(self):
        self.very_low_group = []
        self.low_group = []
        self.medium_group = []
        self.high_group = []
        self.very_high_group = []   
        self.dict_hand_prob = {}
        self.custom_group = []
        with open('poker/hands_prob_preflop.json') as f:
            self.dict_hand_prob = json.load(f)

    def get_dict_hand_prob(self):
        return self.dict_hand_prob
    
    def get_all_tiers_hands(self):
        for hand in self.dict_hand_prob.keys():
            if self.dict_hand_prob[hand] <= 0.09:
                self.very_low_group.append(hand)
            elif self.dict_hand_prob[hand] <= 0.11:
                self.low_group.append(hand)
            elif self.dict_hand_prob[hand] <= 0.15:
                self.medium_group.append(hand)
            elif self.dict_hand_prob[hand] <= 0.2:
                self.high_group.append(hand)
            else:
                self.very_high_group.append(hand)

        return self.very_low_group, self.low_group, self.medium_group, self.high_group, self.very_high_group
    
    def get_very_low_group(self):
        return self.very_low_group
    
    def get_low_group(self):
        return self.low_group
    
    def get_medium_group(self):
        return self.medium_group
    
    def get_high_group(self):
        return self.high_group
    
    def get_very_high_group(self):
        return self.very_high_group
    
    def get_custom_group_by_prob(self, prob):
        for hand in self.dict_hand_prob.keys():
            if self.dict_hand_prob[hand] <= prob:
                self.custom_group.append(hand)
        return self.custom_group