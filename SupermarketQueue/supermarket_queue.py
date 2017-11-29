def queue_time(customers, n):
    if not customers:
        return 0
    list = []
    if len(customers) < n:
        n = len(customers)
    for x in range(0, n):
        list.append(customers[x])
    for x in range(n, len(customers)):
        list[list.index(min(list))] += customers[x]
    return max(list)