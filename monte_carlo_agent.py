class MonteCarloAgent:
    def __init__(self, alpha, gamma, epsilon):
        super().__init__(alpha, gamma, epsilon)

        self.episode_memory = []

    def store_memory(self, state, action, reward):
        self.episode_memory.append((state, action, reward))

    def update():
        G = 0
    