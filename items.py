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
            drainStrPotion,
            addStrPotion,
            drainDexPotion,
            addDexPotion,
            drainWisPotion,
            addWisPotion,
            aSword,
            aStaff,
            aBow,
            ]
        do = random.randint(0, len(itemOptions) - 1)
        self.store = itemOptions[do](depth, ID, x, y)
    def getStore(self):
        return self.store 
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
        return False
class woundingPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(depth, 2*(depth+1))
    def useItem(self, pc):
        pc.wound(self.change)
        return False
class drainStrPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(-2, -1)
    def useItem(self, pc):
        pc.modStr(self.change)
        return False
class addStrPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(1, 2)
    def useItem(self, pc):
        pc.modStr(self.change)
        return False
class drainDexPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(-2, -1)
    def useItem(self, pc):
        pc.modDex(self.change)
        return False
class addDexPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(1, 2)
    def useItem(self, pc):
        pc.modDex(self.change)
        return False
class drainWisPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(-2, -1)
    def useItem(self, pc):
        pc.modWis(self.change)
        return False
class addWisPotion(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Potion'
        self.change = random.randint(1, 2)
    def useItem(self, pc):
        pc.modWis(self.change)
        return False
class aSword(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'straight Sword'
        self.modifier = 2
    def useItem(self, pc):
        return pc.attackStr(self.modifier)
class aBow(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'short bow'
        self.modifier = 2
    def useItem(self, pc):
        return pc.attackDex(self.modifier)
class aStaff(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'wooden staff'
        self.modifier = 2
    def useItem(self, pc):
        return pc.attackWis(self.modifier)

    
