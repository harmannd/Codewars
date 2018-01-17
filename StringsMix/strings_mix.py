from operator import itemgetter, attrgetter

class mixer:
    def __init__(self, letter, owner):
        self.letter = letter
        self.owner = owner
        self.count = 1
        

def mix(s1, s2):
    list1 = countLetters(s1, "1")
    list2 = countLetters(s2, "2")

    listMix = combine(list1, [])
    listMix = combine(list2, listMix)

    listMix = sortList(listMix)

    return toString(listMix)

def sortList(listMix):
    listMix = sorted(listMix, key=attrgetter('letter'))
    listMix = sorted(listMix, key=attrgetter('owner'))
    listMix = sorted(listMix, key=attrgetter('count'), reverse=True)

    return listMix

def toString(listMix):
    str = ""
    for x in range(0, len(listMix)):
        if listMix[x].owner == "3":
            listMix[x].owner = "="
        str += listMix[x].owner + ":" + listMix[x].letter * listMix[x].count + "/"
    return str[:-1]

def combine(list, listMix):
    for x in range(0, len(list)):
        index = find(listMix, list[x].letter)
        if index == -1:
            if list[x].count > 1:
                listMix.append(list[x])
        else:
            if list[x].count > listMix[index].count:
                listMix[index] = list[x]
            elif list[x].count == listMix[index].count:
                listMix[index].owner = "3"
    return listMix

def countLetters(str, owner):
    list = []
    for ch in str:
        if ch.islower():
            index = find(list, ch)
            if index == -1:
                list.append(mixer(ch, owner))
            else:
                list[index].count += 1
    return list

def find(list, ch):
    for x in range(0, len(list)):
        if list[x].letter == ch:
            return x
    return -1