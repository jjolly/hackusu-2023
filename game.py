class Game:
    def __init__(self):
        self.state = (0, 0)
        self.board = (40, 20)

    def getBoard(self):
        board = ['+' + '=' * self.board[0] + '+'] + ['|' + ' ' * self.board[0] + '|'] * self.board[1] + ['+' + '=' * self.board[0] + '+']
        x = self.state[0]
        y = self.state[1]
        line = board[y + 1]
        line = line[:x+1] + '#' + line[x+2:]
        board[y + 1] = line
        return board

    def sendCommand(self, cmd):
        if cmd == "RIGHT" and self.state[0] < self.board[0] - 1:
            self.state = (self.state[0] + 1, self.state[1])
        if cmd == "LEFT" and self.state[0] > 0:
            self.state = (self.state[0] - 1, self.state[1])
        if cmd == "DOWN" and self.state[1] < self.board[1] - 1:
            self.state = (self.state[0], self.state[1] + 1)
        if cmd == "UP" and self.state[1] > 0:
            self.state = (self.state[0], self.state[1] - 1)
