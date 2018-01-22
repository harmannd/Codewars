class Roman:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value


def solution(n):
    roman = [
        Roman('M', 1000), Roman('CM', 900), Roman('D', 500), Roman('CD', 400),
        Roman('C', 100), Roman('XC', 90), Roman('L', 50), Roman('XL', 40),
        Roman('X', 10), Roman('IX', 9), Roman('V', 5), Roman('IV', 4), Roman('I', 1)
    ]
    result = ''

    for x in range(0, len(roman)):
        while n >= roman[x].value:
            n -= roman[x].value
            result += roman[x].symbol
    return result