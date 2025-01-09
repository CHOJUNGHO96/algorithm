import sys

sys.setrecursionlimit(10**6)

단어그룹 = []
N = int(sys.stdin.readline())
for _ in range(N):
    단어그룹.append(input())

정답 = 0

for 단어 in 단어그룹:
    기준글자 = 단어[0]
    스택 = []
    카운트 = 0
    for 인덱스, 글자 in enumerate(단어):
        if 글자 in 스택:
            break

        if 인덱스 > 0:
            기준글자 = 단어[인덱스 - 1]
        if 기준글자 != 글자:
            스택.append(기준글자)

        카운트 += 1
        if 카운트 == len(단어):
            정답 += 1

print(정답)
