def order_weight(strng):
    weights = strng.split()
    if len(weights) == 0:
        return ""
    weights.sort(cmp_weights)
    return " ".join(weights)

def weight(str):
    weight = 0
    for ch in str:
        weight += int(ch)
    return weight

def cmp_weights(a, b):
    weightA = weight(a)
    weightB = weight(b)
    if weightA < weightB:
        return -1
    elif weightA > weightB:
        return 1
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0