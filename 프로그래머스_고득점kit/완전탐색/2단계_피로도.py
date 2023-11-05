# 내풀이
def solution(내피로도: int, 던전: list) -> int:
    import itertools

    _내피로도 = 내피로도
    정답 = 0

    # 던전을 돌수있는 모든 수열을 정한다
    던전경우의수 = list(itertools.permutations(던전))

    for 인덱스, 던전값 in enumerate(던전경우의수):
        for 최소피로도, 피로도 in 던전값:
            if 최소피로도 <= _내피로도:
                _내피로도 -= 피로도
                정답 += 1

            # 던전을 돌수있는 최대의 횟수가 정답과같다면 더이상 순회하지 않아도 되니깐 바로 return
            if 정답 == len(던전):
                return 정답
        else:
            던전경우의수[인덱스] = 정답
            정답 = 0
            _내피로도 = 내피로도

    return max(던전경우의수)


# 다른사람풀이
solution1 = lambda k, d: max(
    [solution(k - u, d[:i] + d[i + 1 :]) + 1 for i, (m, u) in enumerate(d) if k >= m]
    or [0]
)

# 다른사람풀이2
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution2(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
print(solution(80, [[80, 20], [80, 10], [70, 20], [50, 40], [10, 10]]))
