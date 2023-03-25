class Game:
    def __init__(self):
        self.state = None

    def getBoard(self):
        board = [
                    "+=====================================+",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "|                                     |",
                    "+=====================================+"
                ]
        return board

    def sendCommand(self, cmd):
        pass
