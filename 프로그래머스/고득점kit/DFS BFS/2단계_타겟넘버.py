from collections import deque


# def solution(numbers: list, target: int) -> int:
#     result = 0
#     arr1 = deque([(0, 0)])
#     while arr1:
#         num, idx = deque.popleft(arr1)
#         if idx == len(_numbers):
#             if num == target:
#                 result += 1
#             continue
#
#         arr1.append((num + numbers[idx], idx + 1))
#         arr1.append((num - numbers[idx], idx + 1))
#     return result
#
#
# _numbers = [1, 1, 1, 1, 1]
# _target = 3
#
# print(solution(_numbers, _target))

# 다른사람풀이 카테시안 곱 사용
# def solution(numbers, target):
#     from itertools import product
#
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)
#
#
# _numbers = [1, 1, 1, 1, 1]
# _target = 3
#
# print(solution(_numbers, _target))


# def solution(numbers, target):
#     if not numbers and target == 0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target - numbers[0]) + solution(
#             numbers[1:], target + numbers[0]
#         )
#
#
# _numbers = [1, 1, 1, 1, 1]
# _target = 3
#
# print(solution(_numbers, _target))
