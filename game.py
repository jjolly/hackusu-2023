import room
import creatures

def setCharAt(board, x, y, ch):
    line = board[y + 1]
    line = line[:x + 1] + ch + line[x + 2:]
    board[y + 1] = line

class Game:
    def __init__(self):
        self.pc = creatures.pc()
        self.room = room.room(self.pc)
        self.event = {}
        self.event['pillar'] = False
        self.event['monster'] = 0

    def getBoard(self):
        x = self.pc.x
        y = self.pc.y
        w = self.room.x
        h = self.room.y
        board = ['+' + '=' * w + '+'] + ['|' + ' ' * w + '|'] * h + ['+' + '=' * w + '+']
        setCharAt(board, x, y, '#')
        for ob in self.room.getPillars():
            setCharAt(board, ob[0], ob[1], '*')
        for mon in self.room.getMonsters():
            setCharAt(board, mon.x, mon.y, '@')
        if self.event['pillar']:
            board.append('Ouch! You can\'t go that way!')
            self.event['pillar'] = False
        if self.event['monster'] > 0:
            board.append(f'You attacked the monster for {self.event["monster"]} damage')
            self.event['monster'] = 0
        return board

    def sendCommand(self, cmd):
        x = self.pc.x
        y = self.pc.y
        ox = x
        oy = y
        w = self.room.x
        h = self.room.y
        if cmd == "RIGHT" and x < w - 1:
           x += 1
        if cmd == "LEFT" and x > 0:
           x -= 1
        if cmd == "DOWN" and y < h - 1:
           y += 1
        if cmd == "UP" and y > 0:
           y -= 1
        for ob in self.room.getPillars():
            if ob[0] == x and ob[1] == y:
                x = ox
                y = oy
                self.event['pillar'] = True
                break
        for mon in self.room.getMonsters():
            if mon.x == x and mon.y == y:
                x = ox
                y = oy
                self.event['monster'] = 1
                break
        self.pc.x = x
        self.pc.y = y
