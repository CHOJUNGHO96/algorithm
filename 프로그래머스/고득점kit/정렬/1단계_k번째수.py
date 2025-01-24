# 나의풀이
def solution(_array: list, _commands: list) -> list:
    result = []
    for i in _commands:
        tmp_array = _array[i[0] - 1 : i[1]]
        tmp_array.sort()
        result.append(tmp_array[i[2] - 1])
    return result


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))


# 다른사람 풀이
def solution1(_array, _commands):
    """
    람다식과 map함수를 이용하여 간결하게 풀었지만 가독성은 모르겠음
    """
    return list(map(lambda x: sorted(_array[x[0] - 1 : x[1]])[x[2] - 1], _commands))


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution1(array, commands))
