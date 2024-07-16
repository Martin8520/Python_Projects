def minRemoveToMakeValid(s: str) -> str:
    stack = []
    invalid_indices = set()

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                invalid_indices.add(i)

    while stack:
        invalid_indices.add(stack.pop())

    result = []
    for i, char in enumerate(s):
        if i not in invalid_indices:
            result.append(char)

    return ''.join(result)


print(minRemoveToMakeValid("lee(t(c)o)de)"))  # "lee(t(c)o)de"
print(minRemoveToMakeValid("a)b(c)d"))  # "ab(c)d"
print(minRemoveToMakeValid("))(("))  # ""
