def compute_depth(n):
    digits = set([])
    x = 0
    while len(digits) < 10:
        x += 1
        multiple = n * x
        for digit in str(multiple):
            if digit not in digits:
                digits.add(digit)
    return x