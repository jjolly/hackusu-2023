from pyscript import Element
from pyodide.ffi import create_proxy
from game import Game
from collections import Counter

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
            'ArrowRight': "RIGHT",
            'i': "INVENTORY"
        }
    if ch in cmd:
        cmdword = cmd[ch]
        game.sendCommand(cmdword)
        draw_board(game, Element("game-screen"))
        draw_stats(game, Element("stats"))
        draw_messages(game, Element("console"), ch)

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
        if key != "inv":
            stringStats += "\n" + key + " : " + str(value)
        else:
            stringStats += f"\n{key} : {len(value)} of 9"
    window.write(stringStats)

def draw_messages(game, window, ch):
    if ch != "i":
        messages = game.getMessages()
        window.write(messages)
    else:
        inv = game.getStats()["inv"]
        inventoryDict = Counter(inv)
        inventoryString = "Your Inventory : | "
        counter = 1
        for thing, count in inventoryDict.items():
            if counter <= 9:
                inventoryString += f"({counter}) {count} {thing} | "
                counter += 1
        window.write(inventoryString)


gameObject = Game()
draw_board(gameObject, Element("game-screen"))
draw_stats(gameObject, Element("stats"))

js.document.addEventListener('keydown', create_proxy(onKeyPress))