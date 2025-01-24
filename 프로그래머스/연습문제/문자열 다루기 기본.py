def solution1(s):
    return s.isdigit() and len(s) in [4, 6]


def solution(s):
    if len(s) == 4 or len(s) == 6:
        pass
    else:
        return False

    answer = True
    알파벳 = [chr(i) for i in range(97, 123)]
    알파벳 += [chr(i) for i in range(65, 91)]
    for i in s:
        if i in 알파벳:
            answer = False
            break
    return answer


print(solution("123456"))
