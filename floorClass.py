import random
from playerClass import Item
from descriptiongen import basedescgen

class Floor:
    def __init__(self, name = 0):
        self.name = name
        self.root = None
        self.numrooms = 0

    def addroom(self, index):
        if self.root is None:
            self.root = Room(index=index, name=self.numrooms)
            self.numrooms += 1
        else:
            self._addroom(index=index, room=self.root)

    def _addroom(self, index, room):
        if index < room.index:
            if room.rlink1 is not None:
                self._addroom(index=index, room=room.rlink1)
            else:
                room.rlink1 = Room(index=index, name=self.numrooms, lastlink=room.index)
                self.numrooms += 1
        else:
            if room.rlink2 is not None:
                self._addroom(index=index, room=room.rlink2)
            else:
                room.rlink2 = Room(index=index, name=self.numrooms, lastlink=room.index)
                self.numrooms += 1

    def find(self, index):
        if (self.root != None):
            return self._find(index, self.root)
        else:
            return None

    def _find(self, index, room):
        if index == room.index:
            return room
        elif index < room.index and room.rlink1 is not None:
            return self._find(index, room.rlink1)
        elif index > room.index and room.rlink2 is not None:
            return self._find(index, room.rlink2)

    def printFloor(self):
        if self.root is not None:
            self._printFloor(self.root)

    def _printFloor(self, room):
        if room is not None:
            self._printFloor(room.rlink1)
            print(str(room.index) + ' ' + str(room.name) + ' ' + room.desc)
            self._printFloor(room.rlink2)

    def updateFloor(self):
        targetfile = open("currentfloor.txt", "w")
        targetfile.close()
        if self.root is not None:
            self._updateFloor(self.root)

    def _updateFloor(self, room):
        if room is not None:
            self._updateFloor(room.rlink1)
            targetfile = open("currentfloor.txt", "a")
            targetfile.write(str(room.index) + '!' + str(room.name) + '!' + str(room.lastlink) + '!' + room.desc + '!' + room.type + '!' + str(room.stairwell) + '!' + str(room.chest) + '\n')
            targetfile.close()
            self._updateFloor(room.rlink2)

    def floorRoomGen(self):
        if self.root is not None:
            self._floorRoomGen(self.root)

    def _floorRoomGen(self, room):
        if room is not None:
            self._floorRoomGen(room.rlink1)
            room.roomgen()
            self._floorRoomGen(room.rlink2)

    def floorgen(self):
        count = random.randint(50, 80)
        indexlist = random.sample(range(100), count)
        count -= 1
        while count >= 0:
            self.addroom(index=indexlist[count])
            count -= 1
        self.floorRoomGen()


class Room:
    def __init__(self, index = 0, desc = "none", items = Item(), name = -1, type = "none", stairwell = False, chest = False, lastlink = -1):
        self.desc = desc
        self.items = items
        self.name = name
        self.lastlink = lastlink
        self.rlink1 = None
        self.rlink2 = None
        self.index = index
        self.type = type
        self.stairwell = stairwell
        self.chest = chest

    def roomgen(self, store = 0, boss = 0):
        self.descgen()


    def descgen(self):
        self.desc = "You are in Room" + str(self.name) + ':' + basedescgen()
        if self.lastlink != -1:
            self.desc += " There is a door behind you, leading back from where you came."
        if self.rlink1 is not None:
            self.desc += " A door rests to the left." #add an adjective
        if self.rlink2 is not None:
            self.desc += " A door rests to the right."
