def pig_it(text):
    words = text.split(" ")

    for x in xrange(0, len(words)):
        words[x] = words[x][1:len(words[x])] + words[x][0] + "ay"
    return " ".join(words)