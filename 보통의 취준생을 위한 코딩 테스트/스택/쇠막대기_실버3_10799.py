pipe = "()(((()())(())()))(())"
stack = []
result = 0


def soultion(result):
    for i in range(len(pipe)):
        if pipe[i] == "(":
            stack.append(pipe[i])
        elif pipe[i] == ")":
            if pipe[i - 1] == "(":
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1
    print(result)


soultion(result)
