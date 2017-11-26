import re

def count_smileys(arr):
    count = 0
    for face in arr:
        if re.match('[:;][-~]?[)D]', face):
            count += 1
    return count