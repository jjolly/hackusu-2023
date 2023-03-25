'''
class: items

it needs: type

'''

class items:
    def __init__(self, depth, ID, x, y):
        self.x = x
        self.y = y
        self.id = ID
        self.name = 'Trash'
    def getID(self):
        return self.id
    def getName(self):
        return self.name
