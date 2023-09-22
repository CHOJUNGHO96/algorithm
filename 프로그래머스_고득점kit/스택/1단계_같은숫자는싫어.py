"""
주의점
1. 동명이인이 있을수 있음

공략
1. 이름을 key로 묶고 몇명인지 value에 넣어야함
"""


# 나의풀이
def solution(arr: list) -> list:
    answer: list = []
    cnt: int = 0
    for i in arr:
        if cnt == 0:
            answer.append(i)
            cnt += 1
        elif answer[cnt - 1] != i:
            answer.append(i)
            cnt += 1

    return answer


_arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(_arr))


# 다른사람 풀이 - 1
def no_continuous(s):
    """
    배워야할 포인트
    - 스택구조상 선입후출 형태이므로 먼저 [-1:] 로 슬라이스 해서 값을 비교후 같으면 continue 같지않으면 append 해줌
    """
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a


arr = [1, 1, 3, 3, 0, 1, 1]
print(no_continuous(arr))
