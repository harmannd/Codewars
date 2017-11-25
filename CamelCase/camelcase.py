import re

def to_camel_case(text):
    if not text:
        return text
    words = re.split("\_|\-", text)
    for x in xrange(1, len(words)):
        words[x] = words[x][0].capitalize() + words[x][1:]
    return "".join(words)