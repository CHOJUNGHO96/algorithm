"""
알리바바와 40인의 도둑(Bottom-Up)
알리바바는 40인의 도둑으로부터 금화를 훔쳐 도망치고 있습니다.
알리바바는 도망치는 길에 평소에 잘 가지 않던 계곡의 돌다리로 도망가고자 한다.
계곡의 돌다리는 N×N개의 돌들로 구성되어 있다. 각 돌다리들은 높이가 서로 다릅니다.
해당 돌다리를 건널때 돌의 높이 만큼 에너지가 소비됩니다. 이동은 최단거리 이동을 합니다.
즉 현재 지점에서 오른쪽 또는 아래쪽으로만 이동해야 합니다.
N*N의 계곡의 돌다리 격자정보가 주어지면 (1, 1)격자에서 (N, N)까지 가는데 드는 에너지의
최소량을 구하는 프로그램을 작성하세요.
만약 N=3이고, 계곡의 돌다리 격자 정보가 다음과 같다면
3
3 3 5
2 3 4
6 5 2
(1, 1)좌표에서 (3, 3)좌표까지 가는데 드는 최소 에너지는 3+2+3+4+2=14이다.
 ▣입력설명
첫 번째 줄에는 자연수 N(1<=N<=20)이 주어진다.
두 번째 줄부터 계곡의 N*N 격자의 돌다리 높이(10보다 작은 자연수) 정보가 주어진다.
 ▣출력설명
첫 번째 줄에 (1, 1)출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.
 ▣입력예제 1
5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4
 ▣출력예제 1
 25


포인트
1. 1,1 부터 -1,-1 까지는 오른쪽과 아래로만 진행되므로 현재 내위치는 왼쪽 or 위 에서 온값이다.
그러므로 왼쪽,위에서 온값중에서 최솟값만 더해주면된다.
2. 왼쪽 or 위에서만 값을 더해주면되니깐 다이나믹 리스트에 첫번째 행과 첫번째 열에는 값을 미리 세팅해준다.
"""

# 내코드
N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 다이나믹 리스트 세팅
dy = [[-1] * N for _ in range(N)]
dy[0][0] = graph[0][0]
for i in range(N):
    for j in range(N):
        if i == 0 and dy[i][j] == -1 and j != 0:
            dy[i][j] = graph[i][j] + dy[i][j - 1]
        elif j == 0 and dy[i][j] == -1 and i != 0:
            dy[i][j] = graph[i][j] + dy[i - 1][j]


for i in range(1, N):
    for j in range(1, N):
        # 왼쪽 or 위에서만 오니깐 해당값들중 가장 작은값을 더해준다
        if dy[i - 1][j] >= dy[i][j - 1]:
            dy[i][j] = dy[i][j - 1] + graph[i][j]
        else:
            dy[i][j] = dy[i - 1][j] + graph[i][j]

print(dy[-1][-1])

# 강의코드
import sys

sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    dy[0][0] = arr[0][0]
    for i in range(1, n):
        dy[0][i] = dy[0][i - 1] + arr[0][i]
        dy[i][0] = dy[i - 1][0] + arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i - 1][j], dy[i][j - 1]) + arr[i][j]
    print(dy[n - 1][n - 1])
