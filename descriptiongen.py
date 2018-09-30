from random import randrange

def random_line(afile):
    infile = open(afile, 'r')
    line = next(infile)
    for num, aline in enumerate(infile):
      if randrange(num + 2): continue
      line = aline
    infile.close()
    return line


def replacestring(target):
    buffer = target.replace('!', random_line("adjectives.txt"))
    result = buffer.replace('?', random_line("nouns.txt"))
    return result

def basedescgen():
    description = random_line("room1.txt") + ' ' + random_line("room2.txt") + ' ' + random_line("room3.txt") + ' ' + random_line("room4.txt")
    description = description.split()
    counter = 0
    for count in description:
        description[counter] = replacestring(description[counter])
        counter += 1
    description =' '.join(description)
    description = description.replace('\n', '')
    return description