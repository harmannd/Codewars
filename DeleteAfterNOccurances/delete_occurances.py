def delete_nth(order,max_e):
    occurances = {}
    list = []
    for num in order:
        if num not in occurances:
            occurances[num] = 0
        if occurances[num] < max_e:
            occurances[num] = occurances[num] + 1
            list.append(num)
    return list
