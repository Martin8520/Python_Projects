def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


tokens1 = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens1))  # 9

tokens2 = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens2))  # 6

tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens3))  # 22
