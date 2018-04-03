def solve(a, b):
    count = 0
    for x in range(a, b):
        digits = str(x)
        #single digit case
        if len(digits) == 1:
            if digits[0] == '0' or digits[0] == '1' or digits[0] == '8':
                count += 1
        #multiple digits
        else:
            if looper(digits):
                count += 1
    return count

def looper(digits):
    for x in range(0, int(len(digits) / 2)):
        #if not opposites, fail out
        if opposites(digits[x], digits[len(digits) - 1 - x]) == False:
            return False
    #if odd and middle digit isn't a 018 fail out
    if len(digits) % 2 != 0:
        middle = digits[int(len(digits) / 2)]
        if middle != '0' and middle != '1' and middle != '8':
            return False
    #digits are flippable
    return True

def opposites(x, y):
    if x == y == '0':
        return True
    if x == y == '1':
        return True
    if x == y == '8':
        return True
    if x == '6' and y == '9' or x == '9' and y == '6':
        return True
    return False