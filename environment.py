from action import Action

class Grid:
    def init(self, rows, cols, start, end, walls, max_steps):
        self.grid = [[-1] * cols for _ in range(rows)]
        self.grid[end[0]][end[1]] = 0

        self.start = start
        self.walls = walls
        self.state = start
        self.max_steps = max_steps
        self.steps = 0

    def step(self, action):
        self.steps += 1
        next_state = self.state
        reward = None
        done = None
        
        state = self.state

        row, col = self.state[0], self,state[1]

        if action == Action.UP.value and self._is_valid(row + 1, col):
            next_state = [state[0] + 1, state[1]]
        elif action == Action.DOWN.value and self._is_valid(row - 1, col):
            next_state = [state[0] - 1, state[1]]
        elif action == Action.LEFT.value and self._is_valid(row, col - 1):
            next_state = [state[0], state[1] - 1]
        elif action == Action.RIGHT.value and self._is_valid(row, col + 1):
            next_state = [state[0], state[1] + 1]

        reward = self.grid[next_state[0]][next_state[1]]
        done = reward == 0 or self.steps == self.max_steps

        return (next_state, reward, done)

    def _is_valid(self, row, col):
        if row < 0 or row >= len(self.grid):
            return False

        if col < 0 or col >= len(self.grid[0]):
            return False

        return [row, col] not in self.walls