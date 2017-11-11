def unique_in_order(iterable):
    chars = list(iterable)
    unique = []
    if len(chars) == 0:
        return unique
    unique.append(chars[0])
    for x in xrange(1, len(chars)):
        if chars[x] != unique[-1]:
            unique.append(chars[x])
    return unique