import json

class Tiers:
    def __init__(self):
        with open('poker/hands_prob_preflop.json') as f:
            self.dict_hand_prob = json.load(f)
            f.close()
        
        self.very_low_group = [x.split(',') for x in self.dict_hand_prob.keys() if self.dict_hand_prob[x] > -0.1]
        self.low_group = [x.split(',')  for x in self.dict_hand_prob.keys() if self.dict_hand_prob[x] > 0.09]
        self.medium_group = [x.split(',')  for x in self.dict_hand_prob.keys() if self.dict_hand_prob[x] > 0.11]
        self.high_group = [x.split(',')  for x in self.dict_hand_prob.keys() if self.dict_hand_prob[x] > 0.15]
        self.very_high_group = [x.split(',')  for x in self.dict_hand_prob.keys() if self.dict_hand_prob[x] > 0.2]

    def get_dict_hand_prob(self):
        return self.dict_hand_prob
    
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
