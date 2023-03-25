'''
class: items

it needs: type

'''
import random
class createItems:
    def __init__(self, depth, ID, x, y):
        itemOptions = [
            items,
            healthPotion,
            woundingPotion,
            ]
        do = randint(0, len(itemOptions))
        return itemOptions[do](depth, ID, x, y)
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
    def useItem(self, pc):
        return False
class healthPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(depth, 2*(depth+1))
    def useItem(self, pc):
        pc.wound(-self.change)
class woundingPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(depth, 2*(depth+1))
    def useItem(self, pc):
        pc.wound(self.change)
