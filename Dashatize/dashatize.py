def dashatize(num):
    if num is None:
        return "None"

    num = list(str(abs(num)))
    if len(num) == 1:
        return num[0]
    dashNum = num[0]
    if isOdd(num[0]):
        dashNum += "-"

    if len(num) > 2:
        for x in xrange(1, len(num) - 1):
            if isOdd(num[x]):
                dashNum += endingDash(dashNum)
                dashNum += num[x] + "-"
            else:
                dashNum += num[x]

    if isOdd(num[len(num) - 1]):
        dashNum += endingDash(dashNum)
    dashNum += num[len(num) - 1]

    return dashNum

def isOdd(num):
    return int(num) % 2 != 0

def endingDash(dashNum):
    if dashNum[-1:] != "-":
        return "-"
    return ""
