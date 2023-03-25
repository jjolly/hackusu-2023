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
import creatures
import items
class room:
    __slots__ = ['x', 'y', 'pillars', 'pc', 'endCondition', 'monsters', 'level', 'items', 'exit']
    def __init__(self, pc):
        self.level = 0
        self.pc = pc
        self.createNewRoom()
    def createNewRoom(self):
        # set up room size and level
        self.x = random.randint(20, 35)
        self.y = random.randint(10, 15)
        # set up pillars
        create = random.randint(1,20)
        self.pillars = []
        for i in range(create):
            tempX = random.randint(1, self.x-1)
            tempY = random.randint(1, self.y-1)
            if [tempX,tempY] not in self.pillars:
                self.pillars.append([tempX, tempY])
        # set up player and location
        looking = True
        while (looking):
            tempX = random.randint(1, self.x-1)
            tempY = random.randint(1, self.y-1)
            if [tempX, tempY] not in self.pillars:
                looking = False
        self.pc.setX(tempX)
        self.pc.setY(tempY)
        # set up where to avoid
        avoid = self.pillars.copy()
        avoid.append([tempX, tempY])
        # set up end condition
        self.endCondition = False
        # set up monsters
        create = random.randint(1,10)
        created = 0
        self.monsters = []
        while (created < create):
            looking = True
            while (looking):
                tempX = random.randint(1, self.x-1)
                tempY = random.randint(1, self.y-1)
                if [tempX, tempY] not in avoid:
                    looking = False
                    avoid.append([tempX,tempY])
            mon = creatures.randomMonster(self.level, created, tempX, tempY)
            mon = mon.getStore()
            self.monsters.append(mon)
            created += 1
        # set up items
        create = random.randint(1,10)
        created = 0
        self.items = []
        while (created < create):
            looking = True
            while (looking):
                tempX = random.randint(1, self.x-1)
                tempY = random.randint(1, self.y-1)
                if [tempX, tempY] not in self.pillars:
                    looking = False
                    avoid.append([tempX,tempY])
            item = items.createItems(self.level, created, tempX, tempY)
            self.items.append(mon)
            created += 1
        self.level += 1
        self.exit = False
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
    def returnExit(self):
        return self.exit
    def setupExit(self):
        avoid = []
        avoid.append(self.pc.getPosition())
        avoid += self.pillars
        use = self.getItems()
        for i in use:
            avoid.append(i)
        looking = True
        while (looking):
            tempX = random.randint(1, self.x-1)
            tempY = random.randint(1, self.y-1)
            if [tempX, tempY] not in avoid:
                self.looking = False
                avoid.append([tempX,tempY])
                self.exit = [tempX,tempY]
    def removeMonster(self, monsterID):
        deleted = False
        for i in range(0,len(self.monsters) - 1):
            if self.monsters[i].getID() == monsterID:
                deleted = True
                self.monsters.pop(i)
        if len(self.monsters) <= 0:
            self.endCondition = True
            self.setupExit()
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
        return False
    def pickupItem(self, x, y):
        for i in self.items:
            if i.x == x and i.y == y:
                pc.addInventory(i)
                self.removeItem(i.getID())
                return True
        raise('ATTEMPTING TO PICK UP AN ITEM THAT DOES NOT EXIST')
