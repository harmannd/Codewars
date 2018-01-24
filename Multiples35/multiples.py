class Multiple:
    def __init__(self):
        self.set = set()
        self.multiples = []

def solution(number):
    multiple = Multiple()
    getMultiples(number, 3, multiple)
    getMultiples(number, 5, multiple)
    sum = 0
    for x in range(0, len(multiple.multiples)):
        sum += multiple.multiples[x]
    return sum

def getMultiples(number, mult, multiple):
    i = 1
    p = mult
    while p < number:
        if p not in multiple.set:
            multiple.set.add(p)
            multiple.multiples.append(p)
        i += 1
        p = mult * i

