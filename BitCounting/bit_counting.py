def countBits(n):
    count = 0
    for digit in bin(n)[2:]:
        if digit == '1':
            count += 1
    return count