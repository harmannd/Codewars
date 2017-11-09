def iq_test(numbers):
    nums = numbers.split()
    evenCount = oddCount = 0
    evenPosition = oddPosition = 0

    for x in xrange(0, len(nums)):
        if int(nums[x]) % 2 == 0:
            evenCount += 1
            evenPosition = x + 1
        else:
            oddCount += 1
            oddPosition = x + 1
        if oddCount > 1 and evenCount == 1:
            return evenPosition
        if evenCount > 1 and oddCount == 1:
            return oddPosition