'''
class for room

it will need:
x y sizes
pillar locations
monsters
pc
end condition
level
items
'''
import random
import creature
import items
class room:
    __slots__ = ['x', 'y', 'pillars', 'pc', 'endCondition', 'monsters', 'level', 'items',]
    def __init__(self, pc, level):
        # set up room size and level
        self.x = random.randint(20, 35)
        self.y = random.randint(10, 15)
        self.level = level
        # set up pillars
        create = self.random(1,20)
        self.pillars = []
        for i in range(create):
            tempX = random.randint(1, self.x-1)
            tempY = random.randint(1, self.y-1)
            if [tempX,tempY] not in self.pillars:
                self.pillars.append([tempX, tempY])
        # set up player and location
        self.pc = pc
        looking = False
        while (looking):
            tempX = random.randint(1, self.x-1)
            tempY = random.randint(1, self.y-1)
            if [tempX, tempY] not in self.pillars:
                self.looking = True
        self.pc.setX(tempX)
        self.pc.setY(tempY)
        # set up where to avoid
        avoid = self.pillars.copy
        avoid.append([tempX, tempY])
        # set up end condition
        self.endCondition = False
        # set up monsters
        create = self.random(1,10)
        created = 0
        self.monsters = []
        while (created < create):
            looking = False
            while (looking):
                tempX = random.randint(1, self.x-1)
                tempY = random.randint(1, self.y-1)
                if [tempX, tempY] not in self.pillars:
                    self.looking = True
                    avoid.append([tempX,tempY])
            mon = creature.monster(self.level, created, tempX, tempY)
            sel.monsters.append(mon)
        # set up items
        create = self.random(1,10)
        created = 0
        self.items = []
##        while (created < create):
##            looking = False
##            while (looking):
##                tempX = random.randint(1, self.x-1)
##                tempY = random.randint(1, self.y-1)
##                if [tempX, tempY] not in self.pillars:
##                    self.looking = True
##                    avoid.append([tempX,tempY])
##            item = items.items(self.level, created, tempX, tempY)
##            sel.items.append(mon)
    # getters and setters
    def getPillars(self):
        return self.pillars
    def getMonsters(self):
        return self.monsters
    def getItems(self):
        return self.items
    def getLevel(self):
        return self.level
    def getEndCondition(self):
        return self.endCondition
    def removeMonster(self, monsterID):
        deleted = False
        for i in range(self.monsters):
            if self.monsters[i].getID() == monsterID:
                deleted = True
                self.monsters.pop(i)
        if not deleted:
            raise('ATTEMPTING TO DESTROY A MONSTER THAT DOES NOT EXIST')
        return True
    def removeItem(self, itemID):
        deleted = False
        for i in range(self.items):
            if self.items[i].getID() == itemID:
                deleted = True
                self.items.pop(i)
        if not deleted:
            raise('ATTEMPTING TO REMOVE AN ITEM THAT DOES NOT EXIST')
        return True
    def damageMonster(self, monsterID, damage):
        for i in self.monsters:
            if i.id == monsterID:
                i.wound(damage)
                if i.getHP() <= 0:
                    self.removeMonster(monsterID)
                return True
        raise('ATTEMPTING TO ATTACK AN ENEMY THAT DOES NOT EXIST')
    def pickupItem(self, x, y):
        for i in self.items:
            if i.x == x and i.y == y:
                pc.addInventory(i)
                self.removeItem(i.id)
                return True
        raise('ATTEMPTING TO PICK UP AN ITEM THAT DOES NOT EXIST')
