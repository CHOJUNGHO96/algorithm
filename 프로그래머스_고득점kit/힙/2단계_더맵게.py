# 나의풀이
def solution(_scoville: list, _K: int) -> int:
    """
    heapq 모듈을 이용하여 최소힙 연산을 통해 접근을한다.
    """
    import heapq

    answer = 0
    heapq.heapify(_scoville)
    while _scoville[0] < _K:
        if len(_scoville) >= 2:
            first_min = heapq.heappop(_scoville)
            second_min = heapq.heappop(_scoville)
        else:
            answer = -1
            break
        heapq.heappush(_scoville, first_min + (second_min * 2))
        answer += 1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))


# 나의 풀이
def solution1(_scoville: list, _K: int) -> int:
    answer = 0
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    while min(_scoville) < _K:
        if len(_scoville) >= 2:
            tmp = _scoville[:2]
            _scoville = _scoville[2:]
        else:
            answer = -1
            break
        _scoville.append(min(tmp) + (max(tmp) * 2))
        _scoville.sort()
        answer += 1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution1(scoville, K))


# 다른사람 풀이
def solution2(scoville, K):
    import heapq as hq

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1
