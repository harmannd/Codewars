# First attempt
def anagrams1(word, words):
    same = []

    for temp in words:
        if len(temp) == len(word):
            wordDict = seperateIntoDict(word)
            tempDict = seperateIntoDict(temp)
            if wordDict == tempDict:
                same.append(temp)
    return same

def seperateIntoDict(word):
    dict = {}

    for ch in word:
        if ch in dict.keys():
            dict[ch] += 1
        else:
            dict[ch] = 1
    return dict



# Second attempt
def anagrams(word, words):
    same = []

    for temp in words:
        if sorted(word) == sorted(temp):
            same.append(temp)
    return same