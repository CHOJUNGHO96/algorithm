from itertools import permutations


# def solution(numbers: list) -> str:
#     tmp = list(permutations(numbers, len(numbers)))
#     answer = str(max([int("".join(map(str, i))) for i in tmp]))
#     return answer


# def permute(i: int, data: list, result: set):
#     if i == len(data):
#         result.add(int("".join(map(str, data))))
#         return result
#
#     for j in range(i, len(data)):
#         data[j], data[i] = data[i], data[j]
#         permute(j + 1, data, result)
#         data[j], data[i] = data[i], data[j]


# def solution(numbers: list) -> str:
#     result = set()
#     permute(0, numbers, result)
#     return str(max(result))


# def solution(numbers: list) -> str:
#     tmp_dict = {}
#     for i in numbers:
#         tmp_dict.update({(str(i) * 3)[:3]: i})
#     tmp_dict = {
#         k: v
#         for k, v in sorted(tmp_dict.items(), key=lambda item: item[0], reverse=True)
#     }
#
#     return "".join(map(str, tmp_dict.values()))


# def solution(numbers: list) -> str:
#     tmp_dict = {}
#     for i in numbers:
#         tmp_dict.update({(str(i) * 3)[:3]: i})
#     tmp_dict = {
#         k: v
#         for k, v in sorted(tmp_dict.items(), key=lambda item: item[0], reverse=True)
#     }
#
#     return "".join(map(str, tmp_dict.values()))


# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x * 4, reverse=True)
#     answer = "".join(numbers)
#
#     return str(int(answer))


def solution(numbers):
    result = sorted(list(map(str, numbers)), key=lambda i: i * 3, reverse=True)
    return str(int("".join(map(str, result))))


_numbers = [6, 10, 2]
print(solution(_numbers))
