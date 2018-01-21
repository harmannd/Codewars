def wave(str):
    result = []
    for x in range(0, len(str)):
        if str[x].isalpha():
            result.append(str[:x] + str[x].upper() + str[x+1:])
    return result