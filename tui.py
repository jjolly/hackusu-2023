#!/usr/bin/python3
import sys
import os
from game import Game
from getch import getch

def send_command(game, ch):
    cmd = {
            'w': "UP",
            'a': "LEFT",
            's': "DOWN",
            'd': "RIGHT",
            'u': "USE"
          }
    if ch in cmd:
        cmdword = cmd[ch]
        if cmdword == "USE":
            inv = game.getStats()['inv']
            print(f"What needs to go (1-{len(inv)})? ", end='')
            sys.stdout.flush()
            try:
                inum = int(getch())
            except:
                inum = 0
            if inum < 1 or inum > len(inv):
                assert(False)
                return
            cmdword += ' ' + str(inum)
        game.sendCommand(cmdword)

def play_step(game):
    board = game.getBoard()
    os.system('clear')
    for line in board:
        print(line)
    print(game.getMessages())
    stats = game.getStats()
    print(f"HP: {stats['hp']}, Str: {stats['str']}, Dex: {stats['dex']}, Wis: {stats['wis']}, Exp: {stats['exp']}")
    inv = ''
    for i in range(len(stats['inv'])):
        item = stats['inv'][i]
        if len(inv) > 0:
            inv += ', '
        inv += f'{i + 1}:{item}'
    print(f'Inventory: {inv}')
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
