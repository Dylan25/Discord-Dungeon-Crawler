import random


# contains an items damage, value, sellability, whether it's a key, and its' name and description
class Item:
    def __init__(self = 0, dmg = 0, value = 0, sellable = 0, key = 0, name = "Initialized", desc = "Blank"):
        self.dmg = dmg
        self.value = value
        self.sellable = sellable
        self.key = key
        self.name = name
        self.desc = desc


# will contain player health, location, inventory, money, experience, equipped weapon, strength, name
# and Level
class Player:
    def __init__(self, hp=10, location= -1, inventory=[Item(), Item(), Item(), Item(), Item()], money=250, exp=0, equipped="none", strength=1, name="blank", lvl = 1):
        self.hp = hp
        self.location = location
        self.inventory = inventory
        self.money = money
        self.exp = exp
        self.equipped = equipped
        self.strength = strength
        self.name = name
        self.lvl = lvl

    def post(self):
        print(self.hp)

    def readplayer(self):
        playerfile = open(self.name + "player11" + ".txt", 'r')
        filestring = playerfile.read()
        playerfile.close()
        values = filestring.split('\n', filestring.count('\n'))
        self.hp = int(values[0])
        self.location = int(values[1])
        self.money = int(values[2])
        self.exp = int(values[3])
        self.equipped = values[4]
        self.strength = int(values[5])
        self.lvl = int(values[6])

    def update(self):
        userfile = open(self.name + "player11" + ".txt", "w")
        userfile.write(str(self.hp) + '\n')
        userfile.write(str(self.location) + '\n')
        userfile.write(str(self.money) + '\n')
        userfile.write(str(self.exp) + '\n')
        userfile.write(str(self.equipped) + '\n')
        userfile.write(str(self.strength) + '\n')
        userfile.write(str(self.lvl) + '\n')
        userfile.close()

        userinv = open(self.name + "Inventory.txt", "w")
        i = 0
        while (i < 5):
            itemname = self.inventory[i]
            userinv.write(itemname.name + '\n')
            i = i + 1
        userinv.close()

        #uservisits = open(self.name + "Visits.txt", "w")

    def attack(self, target):
        target.hp = target.hp - self.equipped

    def move(self, destination):
        self.location = destination