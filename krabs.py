from playerClass import Player
from floorClass import Floor
import asyncio
from discord.ext import commands
from os import path
from os import listdir
from ast import literal_eval

userlist = []
usernamelist = []

bot = commands.Bot(command_prefix=commands.when_mentioned_or('*'), description='Oh Yeah')

def findPlayer(player):
    i = 0
    for users in userlist:
        if player == userlist[i].name:
            return i
        i += 1

def boolread(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False


def readfloor(targetfile):
    s = ""
    readlevel = Floor()
    infile = open(targetfile, 'r')
    for line in infile.readlines():
        values = line.split('!')
        readlevel.addroom(int(values[0]))
        readlevel.find(int(values[0])).index = int(values[0])
        readlevel.find(int(values[0])).name = int(values[1])
        readlevel.find(int(values[0])).lastlink = int(values[2])
        readlevel.find(int(values[0])).desc = values[3]
        readlevel.find(int(values[0])).type = values[4]
        readlevel.find(int(values[0])).stairwell = literal_eval(values[5])
        print(str(literal_eval(values[5])))
        readlevel.find(int(values[0])).chest = literal_eval(values[6])
        print(str(literal_eval(values[5])))
    print("level read in")
    return readlevel


level = Floor()
level.floorgen()
#level = readfloor("currentfloor.txt")
level.updateFloor()
level.printFloor()



for file in listdir('./'):
    print("in file loop")
    if file.find("player11") != -1:
        user = Player()
        user.name = file.strip("player11.txt")
        user.readplayer()
        userlist.append(user)
        usernamelist.append(user.name)



class commands():
    "game commands"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=False)
    @asyncio.coroutine
    def join(self, ctx):
        """:If you are new, use this to start playing."""
        user = Player()
        user.name = str(ctx.message.author)
        author = str(ctx.message.author)
        if not path.isfile(str(ctx.message.author) + "player11" + ".txt"):
            userlist.append(user)
            usernamelist.append(user.name)
            userlist[findPlayer(author)].update()
            userlist[findPlayer(author)].update()
            userlist[findPlayer(author)].move(level.root.index)
            userlist[findPlayer(author)].update()
            yield from self.bot.send_message(ctx.message.author, "Welcome" + str(ctx.message.author) + ' ' + level.find(user.location).desc)
        else:
            yield from self.bot.send_message(ctx.message.author, "You are already a registered user.")
            del user

    @commands.command(pass_context=True, no_pm=False)
    @asyncio.coroutine
    def move(self, ctx):
        """:use this to move "left", "right", or "back"."""
        userinput = ctx.message.content
        author = str(ctx.message.author)
        userinput = userinput.lower()
        if userinput.find("left") != -1:
            userlist[findPlayer(author)].move(level.find(userlist[findPlayer(author)].location).rlink1.index)
            userlist[findPlayer(author)].update()
            yield from self.bot.send_message(ctx.message.author, level.find(userlist[findPlayer(author)].location).desc)
        elif userinput.find("right") != -1:
            userlist[findPlayer(author)].move(level.find(userlist[findPlayer(author)].location).rlink2.index)
            userlist[findPlayer(author)].update()
            yield from self.bot.send_message(ctx.message.author, level.find(userlist[findPlayer(author)].location).desc)
        elif userinput.find("back") != -1:
            userlist[findPlayer(author)].move(level.find(userlist[findPlayer(author)].location).lastlink)
            userlist[findPlayer(author)].update()
            yield from self.bot.send_message(ctx.message.author, level.find(userlist[findPlayer(author)].location).desc)
        else:
            yield from self.bot.send_message(ctx.message.author, "Unrecognised command")

    @commands.command(pass_context=True, no_pm=False)
    @asyncio.coroutine
    def info(self, ctx):
        """:use this to get a description of the current room."""
        author = str(ctx.message.author)
        print(author)
        print(str(userlist[findPlayer(author)].name))
        print(str(userlist[findPlayer(author)].location))
        yield from self.bot.send_message(ctx.message.author, "you observe that " + level.find(userlist[findPlayer(author)].location).desc)



bot.add_cog(commands(bot))




#bot.login('user', 'pass')
#print('working')
bot.run('token')
print('double working')
