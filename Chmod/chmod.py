def chmod_calculator(perm):
    chmod = list("000")
    for key, value in perm.items():
        if key == 'user':
            chmod[0] = set_value(list(value))
        elif key == 'group':
            chmod[1] = set_value(list(value))
        else:
            chmod[2] = set_value(list(value))
    return "".join(chmod)

def set_value(value):
    mod = 0
    if value[0] != '-':
        mod += 4
    if value[1] != '-':
        mod += 2
    if value[2] != '-':
        mod += 1
    return str(mod)