'''
class for pc

it will need:
strength
dexterity
wisdom
x
y
life
level
exp
type
inventory
'''
class creatures:
    def __init__(self, ty):
        self.baseStats ={
            'sword':[10, 5,4,3],

            'spider':[2,2,3,2],
            }
        self.hp = self.baseStats[ty][0]
        self.str = self.baseStats[ty][1]
        self.dex = self.baseStats[ty][2]
        self.wis = self.baseStats[ty][3]
        self.type = ty
    def getHP(self):
        return self.hp
    def wound(self, damage):
        self.hp -= damage
    def getPosition(self):
        return [self.x, self.y]
    def getStats(self):
        return [self.str, self.dex, self.wis]
    def getType(self):
        return self.ty
    def modStr(self, mod):
        self.str += mod
    def modDex(self, mod):
        self.dex += mod
    def modWis(self, mod):
        self.wis += mod
    def attack(self):
        return self.str/2
    def setY(self, y):
        self.y = y
    def setX(self, x):
        self.x = x
class monster(creatures):
    def __init__(self,depth, ID, x, y, ty = 'spider'):
        super().__init__(ty)
        self.hp = self.hp ** depth
        self.str = self.str ** depth
        self.dex = self.dex ** depth
        self.wis = self.wis ** depth
        self.x = x
        self.y = y
        self.id = ID
    def getID(self):
        return self.id
class pc(creatures):
    def __init__(self, ty = 'sword'):
        self.level = 1
        self.exp = 0
        self.x = 1
        self.y = 1
        self.inventory = [ty]
    def getInventory(self):
        return self.inventory
    def addInventory(self, item):
        self.inventory.append(item)
    def getItem(self, index):
        if index < len(self.inventory):
            return self.inventory[index]
        else:
            raise('ATTEMPTING TO USE ITEM THAT DOES NOT EXIST')
    
        
