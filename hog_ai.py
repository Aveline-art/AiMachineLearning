import math
import random

class HogAI():
    actions = [i for i in range(11)]

    def __init__(self, alpha=0.5, epsilon=0.1) -> None:
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon
    
    def get_q(self, state, action):
        return self.q.get((state, action), 0)
    
    def set_q(self, state, action, value):
        self.q[(state, action)] = value
    
    def update(self, old_state, new_state, action, reward=0):
        old_value = self.get_q(old_state, action)
        new_value = old_value + self.alpha * (self.new_value_estimate(new_state, reward) - old_value)
        self.set_q(old_state, action, new_value)
    
    def new_value_estimate(self, state, reward):
        return reward + self.highest_future_reward(state)
    
    def highest_future_reward(self, state):
        return max([self.get_q(state, action) for action in self.actions])
    
    def make_move(self, state):
        best_value = -math.inf
        best_action = []
        for action in self.actions:
            value = self.get_q(state, action)
            if value > best_value:
                best_action = []
                best_action.append(action)
                best_value = value
            elif value == best_value:
                best_action.append(action)
        
        choice = random.choices([random.choice(self.actions), random.choice(best_action)], weights = [self.epsilon, 1-self.epsilon], k=1)
        return choice[0]
    
    def make_best_move(self, state):
        best_value = -math.inf
        best_action = []
        for action in self.actions:
            value = self.get_q(state, action)
            if value > best_value:
                best_action = []
                best_action.append(action)
                best_value = value
            elif value == best_value:
                best_action.append(action)
        return random.choice(best_action)
    
