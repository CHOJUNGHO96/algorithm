"""
주의점
1. 무조건 다양한 포켓몬을 가져야함
2. nums 의 갯수에서 나누기 2한 마리의 포켓몬을 선택하는중 가장 다양한 갯수 리턴
3. 나누기 2한 값이 넘어갈경우 나누기 2한값으로 리턴

공략
1. key로 묶어서 활용해야함
"""


# 나의풀이
def solution(arg: list) -> int:
    _arg: set = set(arg)
    result: int = len(list(_arg))
    if result >= len(arg) / 2:
        return int(len(arg) / 2)
    else:
        return result


nums = [3, 3, 3, 2, 2, 4]
print(solution(nums))


# 다른사람 풀이
def solution(ls):
    """
    배워야할 포인트
    - min 을 활용하여 최솟값만 나오도록 간결하게 수정이 필요함
    """
    return min(len(ls) / 2, len(set(ls)))
