def solve(st):
    if st[0].isdigit():
        return int(st[0]) * solve(st[1:])
    elif st[0].isalpha():
        return (st[0] + solve(st[1:]))
    elif st[0] == '(':
        return solve(st[1:])
    else:
        return ''
