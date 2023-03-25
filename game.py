import room
import creatures

class Game:
    def __init__(self):
        self.pc = creatures.pc()
        self.room = room.room(self.pc)

    def getBoard(self):
        x = self.pc.x
        y = self.pc.y
        w = self.room.x
        h = self.room.y
        board = ['+' + '=' * w + '+'] + ['|' + ' ' * w + '|'] * h + ['+' + '=' * w + '+']
        line = board[y + 1]
        line = line[:x+1] + '#' + line[x+2:]
        board[y + 1] = line
        return board

    def sendCommand(self, cmd):
        x = self.pc.x
        y = self.pc.y
        w = self.room.x
        h = self.room.y
        if cmd == "RIGHT" and x < w - 1:
           self.pc.setX(x + 1)
        if cmd == "LEFT" and x > 0:
           self.pc.setX(x - 1)
        if cmd == "DOWN" and y < h - 1:
           self.pc.sety(y + 1)
        if cmd == "UP" and y > 0:
           self.pc.setY(y - 1)
