directions = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}


def dirReduc(arr):
    x = 0
    while x < len(arr) - 1:
        if directions[arr[x]] == arr[x + 1]:
            del arr[x]
            del arr[x]
            if x != 0:
                x = x - 1
        else:
            x += 1
    return arr