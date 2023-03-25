from pyscript import Element
from pyodide.ffi import create_proxy
from game import Game

def onKeyPress(event):
    event.preventDefault();
    
    send_command(gameObject, event.key)



def current_key(key):
    # Get paragraph element by id
    return key, 1


def send_command(game, ch):
    cmd = {
            'w': "UP",
            'a': "LEFT",
            's': "DOWN",
            'd': "RIGHT",
            'ArrowUp': "UP",
            'ArrowLeft': "LEFT",
            'ArrowDown': "DOWN",
            'ArrowRight': "RIGHT"
        }
    if ch in cmd:
        game.sendCommand(cmd[ch])
        draw_board(game, Element("game-screen"))
        draw_stats(game, Element("stats"))
        draw_messages(game, Element("console"))

def draw_board(game, window):
    board = game.getBoard()
    stringBoard = ""
    for line in board:
        stringBoard += "\n" + line
    window.write(stringBoard)

def draw_stats(game, window):
    playerStats = game.getStats()
    stringStats = ""
    for key in playerStats:
        value = playerStats[key]
        stringStats += "\n" + key + " : " + str(value)
    window.write(stringStats)

def draw_messages(game, window):
    message = game.getMessages()
    window.write(message)


gameObject = Game()
draw_board(gameObject, Element("game-screen"))
draw_stats(gameObject, Element("stats"))

js.document.addEventListener('keydown', create_proxy(onKeyPress))