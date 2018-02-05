def solve(s):
    count = 0
    for x in range(0, len(s)):
        for y in range(x + 1, len(s) + 1):
            if int(s[x:y]) % 2 != 0:
                count += 1
    return count