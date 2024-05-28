"""
가방문제(냅색 알고리즘)
최고 17kg의 무게를 저장할 수 있는 가방이 있다. 그리고 각각 3kg, 4kg, 7kg, 8kg, 9kg의
무게를 가진 5종류의 보석이 있다. 이 보석들의 가치는 각각 4, 5, 10, 11, 13이다.
이 보석을 가방에 담는데 17kg를 넘지 않으면서 최대의 가치가 되도록 하려면 어떻게 담아야
할까요? 각 종류별 보석의 개수는 무한이 많다. 한 종류의 보석을 여러 번 가방에 담을 수 있
다는 뜻입니다.
 ▣입력설명
첫 번째 줄은 보석 종류의 개수와 가방에 담을 수 있는 무게의 한계값이 주어진다.
두 번째 줄부터 각 보석의 무게와 가치가 주어진다.
가방의 저장무게는 1000kg을 넘지 않는다.  보석의 개수는 30개 이내이다.
 ▣출력설명
첫 번째 줄에 가방에 담을 수 있는 보석의 최대가치를 출력한다.
 ▣입력예제 1
4 11
5 12
3 8
6 14
4 8
 ▣출력예제 1
28
"""
# 내풀이
N, K = map(int, input().split())
dy = [0] * (K + 1)
w = []
v = []
for _ in range(N):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)


for i in range(N):
    # 제한 무개한에서 하나의 무개가 가질수있는 최대치를 기록해준다.
    for j in range(w[i], K + 1):
        if dy[j - w[i]] + v[i] > dy[j]:
            dy[j] = dy[j - w[i]] + v[i]

print(max(dy))


# 강의풀이
import sys

sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m + 1)
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(w, m + 1):
            dy[j] = max(dy[j], dy[j - w] + v)
    print(dy[m])
