def solution(논문: list):
    논문.sort(reverse=True)
    for 인덱스, 책 in enumerate(논문):
        if 인덱스 >= 책:
            return 인덱스
    return len(논문)


# _citations = [3, 0, 6, 1, 5]
# _citations = [0, 1, 3, 4, 5, 6]
print(solution([2, 2, 2, 2, 2, 6]))  # 3
# print(solution([3, 0, 6, 1, 5]))  # 3
# print(solution([10, 8, 5, 4, 3]))  # 4
# print(solution([25, 8, 5, 3, 1]))  # 3
# print(solution([8, 7, 7, 6, 5, 5, 3]))  # 5
# print(solution([47, 42, 32, 28, 24, 22, 17, 15, 10, 10, 8]))  # 10
# print(solution([12, 11, 10, 9, 8, 1]))  # 5
# print(solution([6, 6, 6, 6, 6, 1]))  # 5
# print(solution([20, 21, 22, 23]))  # 4
# print(solution([4, 4, 4]))  # 3
# print(solution(_citations))
