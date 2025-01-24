# 내 두번째풀이
def solution(operations: list) -> list:
    """
    포인트
    최대힙(nlargest 이용)과 최소힙의 속성을 이용하여 풀이진행
    """
    import heapq

    최소힙 = []
    최대힙 = []

    for 명령어 in operations:
        if 명령어[0] == "I":
            heapq.heappush(최소힙, int(명령어[2:]))
            heapq.heappush(최대힙, int(명령어[2:]))

        # 최대힙으로 만들어주기위해 nlargest() 를 사용한다
        # ex : [-45, 653] -> [653, -45]
        최대힙 = heapq.nlargest(len(최대힙), 최대힙)

        # 둘다 없을경우 continue
        if not 최대힙 and not 최소힙:
            continue

        # 최댓값 삭제일 경우 최대힙 은 첫번째 요소삭 제, 최소힙 은 마지막 요소 삭제
        if 명령어 == "D 1":
            heapq.heappop(최대힙)
            최소힙.pop()

        # 최솟값 삭제일 경우 최소힙 은 첫번째 요소 삭제 최대힙 은 마지막 요소 삭제
        elif 명령어 == "D -1":
            heapq.heappop(최소힙)
            최대힙.pop()

    # 최대힙 , 최소힙 둘다 값이 없을 경우 [0,0] 리턴
    if not 최대힙 and not 최소힙:
        return [0, 0]

    # 최대힙 만 값이 있을 경우
    elif 최대힙 and not 최소힙:
        return [최대힙[0], 최대힙[-1]] if len(최대힙) >= 2 else [최대힙[0], 최대힙[0]]

    # 최소힙 만 값이 있을 경우
    elif 최소힙 and not 최대힙:
        return [최소힙[-1], 최소힙[0]] if len(최소힙) >= 2 else [최소힙[0], 최소힙[0]]

    # 최소힙, 최대힙 둘다 값이 있을 경우
    else:
        return [최대힙[0], 최소힙[0]]


# 내 첫번째풀이
def solution2(operations: list) -> list:
    import heapq

    최대힙 = []
    최소힙 = []
    for 명령어 in operations:
        if 명령어[0] == "I":
            if 명령어[2] == "-":
                heapq.heappush(최소힙, int(명령어[2:]))
            else:
                heapq.heappush(최대힙, int(명령어[2:]))

        if 최대힙 and 명령어 == "D 1":
            최대힙.pop()
        elif not 최대힙 and 최소힙 and 명령어 == "D 1":
            최소힙.pop()
        elif 최소힙 and 명령어 == "D -1":
            heapq.heappop(최소힙)
        elif not 최소힙 and 최대힙 and 명령어 == "D -1":
            heapq.heappop(최대힙)

    if not 최대힙 and not 최소힙:
        return [0, 0]
    elif 최대힙 and not 최소힙:
        return [최대힙[-1], 최대힙[0]] if len(최대힙) >= 2 else [최대힙[0], 최대힙[0]]
    elif 최소힙 and not 최대힙:
        return [최소힙[-1], 최소힙[0]] if len(최소힙) >= 2 else [최소힙[0], 최소힙[0]]
    else:
        return [최대힙[-1], 최소힙[0]]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0,0]
print(
    solution(
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    )
)  # [333, -45]
print(solution(["I 16", "D 1"]))  # [0,0]
print(solution(["I 7", "I 5", "D -1"]))  # [7,7]
print(
    solution(
        ["I 1", "I 3", "I 5", "I 7", "I 9", "D -1", "D -1", "D 1", "I 2", "D 1", "D 1"]
    )
)  # [2,2]
print(solution(["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"]))  # [40, 40]
