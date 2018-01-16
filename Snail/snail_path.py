class Runner:
    def __init__(self):
        self.direction = 'E'
        self.position = "00"
        self.visited = set([])
        self.numbers = []

    def row(self):
        return int(self.position[0])

    def col(self):
        return int(self.position[1])


def snail(array):
    runner = Runner()

    if array == [[]]:
        return runner.numbers
    runner.visited.add(runner.position)
    runner.numbers.append(array[runner.row()][runner.col()])
    while True:
        if len(runner.numbers) == twoDeArrayLen(array):
            return runner.numbers
        runner.position = move(runner, array)
        runner.visited.add(runner.position)
        runner.numbers.append(array[runner.row()][runner.col()])

def twoDeArrayLen(array):
    rows = len(array)
    cols = len(array[0])
    return rows * cols

def move(runner, array):
    if runner.direction == 'E':
        nextPos = str(runner.row()) + str(runner.col() + 1)
        if runner.col() + 1 < len(array[0]) and nextPos not in runner.visited:
            return nextPos
        else:
            runner.direction = 'S'
            return move(runner, array)
    elif runner.direction == 'S':
        nextPos = str(runner.row() + 1) + str(runner.col())
        if runner.row() + 1 < len(array) and nextPos not in runner.visited:
            return nextPos
        else:
            runner.direction = 'W'
            return move(runner, array)
    elif runner.direction == 'W':
        nextPos = str(runner.row()) + str(runner.col() - 1)
        if runner.col() - 1 >= 0 and nextPos not in runner.visited:
            return nextPos
        else:
            runner.direction = 'N'
            return move(runner, array)
    else:
        nextPos = str(runner.row() - 1) + str(runner.col())
        if runner.row() - 1 >= 0 and nextPos not in runner.visited:
            return nextPos
        else:
            runner.direction = 'E'
            return move(runner, array)