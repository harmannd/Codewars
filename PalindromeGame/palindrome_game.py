def solve(str1,str2):
    pl_letters = count_letters(str1)
    p2_letters = count_letters(str2)

    for key in pl_letters.keys():
        if pl_letters[key] > 1 and key not in p2_letters.keys():
            return 1
    return 2


def count_letters(str):
    letters = {}
    for char in str:
        if char in letters.keys():
            letters[char] += 1
        else:
            letters[char] = 1
    return letters