"""
가장 높은 탑 쌓기
밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 한다. 탑은 벽돌을 한 개씩 아래
에서 위로 쌓으면서 만들어 간다. 아래의 조건을 만족하면서 가장 높은 탑을 쌓을 수 있는 프
로그램을 작성하시오.
(조건1) 벽돌은 회전시킬 수 없다. 즉, 옆면을 밑면으로 사용할 수 없다.
(조건2) 밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다.
(조건3) 벽돌들의 높이는 같을 수도 있다.
(조건4) 탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
(조건5) 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.
▣입력설명
입력 파일의 첫째 줄에는 입력될 벽돌의 수가 주어진다. 입력으로 주어지는 벽돌의 수는 최대
100개이다. 둘째 줄부터는 각 줄에 한 개의 벽돌에 관한 정보인 벽돌 밑면의 넓이, 벽돌의 높
이 그리고 무게가 차례대로 양의 정수로 주어진다. 각 벽돌은 입력되는 순서대로 1부터연속적
인 번호를 가진다.
▣출력설명
첫 번째 줄에 가장 높이 쌓을 수 있는 탑의 높이를 출력한다.
▣입력예제 1
5
25 3 4
4 4 6
9 2 3
16 2 5
1 5 2
▣출력예제 1
10
"""

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: [x[0]], reverse=True)
tmp_arr = [-1] * N
tmp_arr[0] = arr[0][1]

for i in range(1, N):
    tmp = 0
    for j in range(i):
        if arr[j][2] > arr[i][2]:
            tmp = max(tmp, tmp_arr[j])
    tmp_arr[i] = tmp + arr[i][1] if tmp != 0 else arr[i][1]

print(max(tmp_arr))

# 강의정답
import sys

sys.stdin = open("input.txt", "r")
if __name__ == "__main__":
    n = int(input())
    bricks = []
    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True)
    dy = [0] * n
    dy[0] = bricks[0][1]
    res = bricks[0][1]
    for i in range(1, n):
        max_h = 0
        for j in range(i - 1, -1, -1):
            if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
                max_h = dy[j]
        dy[i] = max_h + bricks[i][1]
        res = max(res, dy[i])
    print(res)
