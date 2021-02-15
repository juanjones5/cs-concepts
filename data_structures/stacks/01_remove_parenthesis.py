def min_remove_to_make_valid(s: str) -> str:
    """
    Remove the minimum number of parentheses ( '(' or ')',
    in any positions ) so that the resulting parentheses
    string is valid and return any valid string.
    """
    invalid = []
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        if c == ")":
            if stack:
                stack.pop()
            else:
                invalid.append(i)
    to_remove = set(invalid + stack)
    result = ""
    for i, c in enumerate(s):
        if i not in to_remove:
            result += c
    return result
