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
import random
import items
class randomMonster:
    def __init__(self,depth, ID, x, y):
        types = ['spider',
                 'orc',
                 'skeleton',
                 ]
        use = random.randint(0, len(types) - 1)
        use = types[use]
        self.store = monster(depth, ID, x, y, use)
    def getStore(self):
        return self.store
class creatures:
    def __init__(self, ty):
        self.baseStats ={
            # character classes
            'fighter':[random.randint(10,20), random.randint(12,19), random.randint(8,15), random.randint(3, 10), 2],
            'wizard':[random.randint(5,10), random.randint(3,10), random.randint(8,15), random.randint(12, 19), 1],
            'ranger':[random.randint(7,15), random.randint(8,15), random.randint(12,19), random.randint(3, 10), 3],
            # items
            'sword':[10, 5,4,3,1],
            'bow':[7, 4,5,3,1],
            'staff':[5,3,4,5,1],
            # monster section
            'spider':[3,2,3,2,3],
            'orc':[6,4,2,2,1],
            'skeleton':[2,2,3,1,2],
            }
        loc = 0
        self.hp = self.baseStats[ty][loc]
        loc += 1
        self.str = self.baseStats[ty][loc]
        loc += 1
        self.dex = self.baseStats[ty][loc]
        loc += 1
        self.wis = self.baseStats[ty][loc]
        loc += 1
        self.move = self.baseStats[ty][loc]
        loc += 1
        self.ty = ty
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
    def getMove(self):
        return self.move
class monster(creatures):
    def __init__(self,depth, ID, x, y, ty = 'spider'):
        super().__init__(ty)
        self.strength = ['orc']
        self.dexterity = ['spider', 'skeleton']
        self.wisdom = []
        self.hp = self.hp ** depth
        self.str = self.str ** depth
        self.dex = self.dex ** depth
        self.wis = self.wis ** depth
        self.x = x
        self.y = y
        self.id = ID
    def getID(self):
        return self.id
    def attack(self):
        if self.getType() in self.strength:
            return self.str/2
        elif self.getType() in self.dexterity:
            return self.dex/2
        elif self.getType() in self.wisdom:
            return self.wis/2
class pc(creatures):
    def __init__(self, ty = 'sword'):
        super().__init__('fighter')
        starters = {
            'sword':items.aSword,
            'bow':items.aBow,
            'staff':items.aStaff,
            }
        self.level = 1
        self.exp = 0
        self.x = 1
        self.y = 1
        self.equiped = Null
        self.inventory = [ty]
    def getInventory(self):
        return self.inventory
    def addInventory(self, item):
        self.inventory.append(item)
    def getItem(self, index):
        if index < len(self.inventory):
            return self.inventory[starters[ty]()]
        else:
            raise('ATTEMPTING TO USE ITEM THAT DOES NOT EXIST')
    def setEquipped(self, item):
    	self.equipped = item
    def getEquipped(self, item):
    	return self.equipped
    def attack(self):
    	if self.getEquipped():
    		use = self.getEquipped()
    		return use.useItem(self)
    	else:
    		return self.str/2
    def attackStr(self, modifier):
        return self.str*modifier/2
    def attackDex(self, modifier):
        return self.dex*modifier/2
    def attackWis(self, modifier):
        return self.wis*modifier/2
    
        
