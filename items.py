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
            fireball,
            firebolt,
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
class scroll(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'Scroll'
        self.uses = random.randint(1, 5)
        self.change = random.randint(depth * depth / 2, depth * depth)
    def getUses(self):
        return self.uses
    def getName(self):
    	return self.name
class fireball(scroll):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.change = random.randint(depth * depth, depth * depth*2)
    def useItem(self, pc):
        self.uses -= 1
        rand = random.randint(0,10)
        if rand == 5:
            pc.wound(self.change)
            if pc.getHP() <= 0:
                 pc.wound(pc.getHP()-1)
            return 0
        else:
            return self.change + rand 
class firebolt(scroll):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
    def useItem(self, pc):
    	rand = random.randint(0,5)
    	self.uses -= 1
    	return self.change + rand 
            
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
    	if self == pc.getEquipped():
             return pc.attackStr(self.modifier)
    	else:
             pc.setEquipped(self)
class aBow(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'short bow'
        self.modifier = 2
    def useItem(self, pc):
    	if self == pc.getEquipped():
             return pc.attackDex(self.modifier)
    	else:
             pc.setEquipped(self)
class aStaff(items):
    def __init__(self, depth, ID, x, y):
        super().__init__(depth, ID, x, y)
        self.name = 'wooden staff'
        self.modifier = 2
    def useItem(self, pc):
    	if self == pc.getEquipped():
             return pc.attackWis(self.modifier)
    	else:
             pc.setEquipped(self)

    
