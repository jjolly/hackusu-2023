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
        ids = created
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
            item = items.createItems(self.level, ids, tempX, tempY).getStore()
            self.items.append(item)
            created += 1
            ids += 1
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
                looking = False
                avoid.append([tempX,tempY])
                self.exit = [tempX,tempY]
    def removeMonster(self, monsterID):
        deleted = False
        for i in range(0,len(self.monsters)):
            if self.monsters[i].getID() == monsterID:
                deleted = True
                self.monsters.pop(i)
                break
        
        if len(self.monsters) <= 0:
            self.endCondition = True
            self.setupExit()
        return True
    def removeItem(self, itemID):
        deleted = False
        for i in range(0,len(self.items)):
            if self.items[i].getID() == itemID:
                deleted = True
                self.items.pop(i)
                break
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
                self.pc.addInventory(i)
                self.removeItem(i.getID())
                return True
        raise('ATTEMPTING TO PICK UP AN ITEM THAT DOES NOT EXIST')
    def monstersTurn(self):
        for mon in self.monsters:
            avoid = self.pillars.copy()
            for i in self.monsters:
                if i.getID() != mon.getID():
                     avoid.append(i.getPosition())
            # avoid is now set up
            moves = 0
            while moves < mon.getMove():
                 monPos = mon.getPosition()
                 pcPos = pc.getPosition()
                 distY = abs(monPos[1] - pcPos[1])
                 distX = abs(monPos[0] - pcPos[0])
                 looking = True
                 while looking:
                      if distY < distX:
                           if monPos[1] - pcPos[1] < 0:
                                if [monPos[0], monPos[1]+1] == self.pc.getPosition():
                                     damage = mon.attack()
                                     self.pc.wound(damage)
                                     if self.pc.getHP() <= 0:
                                         return True
                                elif [monPos[0], monPos[1]+1] not in avoid:
                                     mon.setY(monPos[1]+1)
                                elif [monPos[0] + 1, monPos[1]] not in avoid:
                                     mon.setX(monPos[0]+1)
                                elif [monPos[0] - 1, monPos[1]] not in avoid:
                                     mon.setX(monPos[0]-1)
                                elif [monPos[0], monPos[1]-1] not in avoid:
                                     mon.setY(monPos[1]-1)
                           else:
                                if [monPos[0], monPos[1]-1] == self.pc.getPosition():
                                     damage = mon.attack()
                                     self.pc.wound(damage)
                                     if self.pc.getHP() <= 0:
                                         return True
                                elif [monPos[0], monPos[1]-1] not in avoid:
                                     mon.setY(monPos[1]-1)
                                elif [monPos[0] - 1, monPos[1]] not in avoid:
                                     mon.setX(monPos[0]-1)
                                elif [monPos[0] + 1, monPos[1]] not in avoid:
                                     mon.setX(monPos[0]+1)
                                elif [monPos[0], monPos[1]+1] not in avoid:
                                     mon.setY(monPos[1]+1)
                      else:
                           if monPos[0] - pcPos[0] < 0:
                                if [monPos[0]+1, monPos[1]] == self.pc.getPosition():
                                     damage = mon.attack()
                                     self.pc.wound(damage)
                                     if self.pc.getHP() <= 0:
                                         return True
                                elif [monPos[0]+1, monPos[1]] not in avoid:
                                     mon.setX(monPos[0]+1)
                                elif [monPos[0], monPos[1]+1] not in avoid:
                                     mon.setY(monPos[1]+1)
                                elif [monPos[0], monPos[1]-1] not in avoid:
                                     mon.setY(monPos[1]-1)
                                elif [monPos[0]-1, monPos[1]] not in avoid:
                                     mon.setX(monPos[0]-1)
                           else:
                                if [monPos[0]-1, monPos[1]] == self.pc.getPosition():
                                     damage = mon.attack()
                                     self.pc.wound(damage)
                                     if self.pc.getHP() <= 0:
                                         return True
                                elif [monPos[0]-1, monPos[1]] not in avoid:
                                     mon.setX(monPos[0]-1)
                                elif [monPos[0], monPos[1]-1] not in avoid:
                                     mon.setY(monPos[1]-1)
                                elif [monPos[0], monPos[1]+1] not in avoid:
                                     mon.setY(monPos[1]+1)
                                elif [monPos[0]-1, monPos[1]] not in avoid:
                                     mon.setX(monPos[0]+1)
                      moves += 1
