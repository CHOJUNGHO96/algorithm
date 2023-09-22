"""
주의점
1. 동명이인이 있을수 있음

공략
1. 이름을 key로 묶고 몇명인지 value에 넣어야함
"""


# 나의풀이
def solution(_participant: list, _completion: list):
    pre_dict: dict = {}
    for name in _participant:
        if name in pre_dict.keys():
            pre_dict[name] += 1
        else:
            pre_dict[name] = 1

    for name in _completion:
        pre_dict[name] -= 1
        if pre_dict[name] == 0:
            del pre_dict[name]

    # yield from list(pre_dict.keys())
    for _ in list(pre_dict.keys()):
        return _


participant: list = ["mislav", "stanko", "mislav", "ana"]
completion: list = ["stanko", "ana", "mislav"]
# print(next(solution(participant, completion)))
print(solution(participant, completion))

# 다른사람 풀이 - 1
def solution1(participant, completion):
    """
    배워야할 포인트
    - collections 을 활용한다
    """
    import collections

    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 다른사람 풀이 - 2
def solution2(participant, completion):
    """
    배워야할 포인트
    - hash 함수를 활용하여 temp에 참가자의 해쉬 인덱스를 더하고 완주자의 해쉬 인덱스를 빼서 남은사람을 구함
    """
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
