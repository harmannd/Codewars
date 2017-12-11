def tops(msg):
    str = ""
    x = y = 1
    while x < len(msg):
        str += msg[x]
        y += 4
        x += y
    return str[::-1]