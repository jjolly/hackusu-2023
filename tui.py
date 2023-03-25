#!/usr/bin/python3
import sys
from game import Game
from getch import getch

def send_command(game, ch):
    cmd = {
            'w': "UP",
            'a': "LEFT",
            's': "DOWN",
            'd': "RIGHT"
          }
    if ch in cmd:
        game.sendCommand(cmd[ch])

def play_step(game):
    board = game.getBoard()
    for line in board:
        print(line)
    print("Whatcha wanna do? ", end = "")
    sys.stdout.flush()
    ch = getch()
    print(ch)
    if ch == 'q':
        print("See ya!")
        return False
    send_command(game, ch)
    return True

def run_game():
    game = Game()
    while True:
        result = play_step(game)
        if not result:
            break

if __name__ == '__main__':
    run_game()
