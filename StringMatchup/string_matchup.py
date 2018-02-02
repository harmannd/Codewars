def solve(a,b):
    dict = {}
    arr = []

    for word in a:
        if word in dict.keys():
            dict[word] += 1
        else:
            dict[word] = 1
    for word in b:
        if word in dict.keys():
            arr.append(dict[word])
        else:
            arr.append(0)
    return arr