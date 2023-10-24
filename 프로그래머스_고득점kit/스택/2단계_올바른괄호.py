def solution(s: str) -> bool:
    cnt = 0

    if s[0] != "(" or s[-1] != ")":
        return False

    for i in s:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1

        if cnt < 0:
            return False

    return True if cnt == 0 else False


_s = "(()("

print(solution(_s))
