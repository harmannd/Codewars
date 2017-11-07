def goodVsEvil(good, evil):
    goodWorth= [1, 2, 3, 3, 4, 10]
    evilWorth = [1, 2, 2, 2, 3, 5, 10]
    goodCount = 0
    evilCount = 0

    good = good.split()
    evil = evil.split()

    for x in xrange(0, len(good)):
       goodCount += int(good[x]) * goodWorth[x]

    for x in xrange(0, len(evil)):
       evilCount += int(evil[x]) * evilWorth[x]

    if goodCount > evilCount:
        return 'Battle Result: Good triumphs over Evil'
    elif goodCount < evilCount:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'