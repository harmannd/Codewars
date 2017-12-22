from sympy.utilities.iterables import multiset_permutations
import numpy as np

def ssc_forperm(arr):
    values = [{"total perm": 0}, {"total ssc": 0}, {"max ssc": ""}, {"min ssc": ""}]
    a = np.array(arr)
    for p in multiset_permutations(a):
        score = special_score(p)
        values[0]["total perm"] += 1
        values[1]["total ssc"] += score
        if values[2]["max ssc"] == "" or score > values[2]["max ssc"]:
            values[2]["max ssc"] = score
        if values[3]["min ssc"] == "" or score < values[3]["min ssc"]:
            values[3]["min ssc"] = score
    return values

def special_score(p):
    score = 0
    for x in range(0, len(p)):
        score += (x + 1) * p[x]
    return score