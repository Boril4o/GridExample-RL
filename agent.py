import random

class Agent:
    def __init__(self, alpha, gamma, epsilon):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        self.action_values = {}

    def choose_action(self, state):
        action = None
        rnd_num = random.random()

        if rnd_num < self.epsilon:
            action = random.randint(0, 4)
        else:
            values = self.action_values.get(state)

            if values:
                action = values.index(max(values))
            else:
                action = 0

        return action

    def update():
        pass