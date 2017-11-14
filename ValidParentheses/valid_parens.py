def valid_parentheses(string):
    chars = list(string)
    stack = []

    for char in chars:
        if char == "(":
            stack.append(char)
        if char == ")":
            if len(stack) == 0:
                return False
            temp = stack.pop()
    if len(stack) != 0:
        return False
    return True