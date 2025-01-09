"""
문자열 s는 아래 조건을 만족하면 **행복한 문자열(happy string)**이라고 합니다:

s는 오직 문자 'a', 'b', 'c'만 포함합니다.
s는 "aaa", "bbb", "ccc"와 같은 문자열을 **부분 문자열(substring)**로 포함하지 않습니다.
s는 'a' 문자가 최대 a번만 포함될 수 있습니다.
s는 'b' 문자가 최대 b번만 포함될 수 있습니다.
s는 'c' 문자가 최대 c번만 포함될 수 있습니다.
정수 a, b, c가 주어질 때, 가장 긴 행복한 문자열을 반환하세요. 가장 긴 문자열이 여러 개라면, 아무거나 반환해도 됩니다.
만약 그러한 문자열이 존재하지 않는다면, 빈 문자열 ""을 반환하세요.

부분 문자열은 문자열 내의 연속된 문자 시퀀스를 의미합니다.
"""
from collections import deque


class Solution:
    @classmethod
    def longestDiverseString(cls, a: int, b: int, c: int) -> str:
        정답 = []
        플래그 = deque([])
        if a > 0:
            플래그.append([a, "a"])
        if b > 0:
            플래그.append([b, "b"])
        if c > 0:
            플래그.append([c, "c"])
        while 플래그:
            플래그 = deque(sorted(플래그, reverse=True))
            단어수, 단어 = 플래그.popleft()

            if len(정답) >= 2:
                if 정답[-2:] != [단어, 단어] and 단어수 > 0:
                    if 단어수 > 0:
                        단어수 -= 1
                        정답.append(단어)
                        if 단어수 > 0:
                            플래그.append([단어수, 단어])
                else:
                    if 정답[-2:] == [단어, 단어]:
                        단어수2, 단어2 = 플래그.popleft()
                        단어수2 -= 1
                        정답.append(단어2)
                        if 단어수2 > 0:
                            플래그.append([단어수2, 단어2])
                        if 단어수 > 0:
                            플래그.append([단어수, 단어])
            else:
                단어수 -= 1
                정답.append(단어)
                if 단어수 > 0:
                    플래그.append([단어수, 단어])

            if len(플래그) == 1 and 정답[-2:] == [플래그[0][1], 플래그[0][1]]:
                break

        return "".join(map(str, 정답))


print(Solution.longestDiverseString(a=2, b=2, c=1))
print(Solution.longestDiverseString(a=0, b=8, c=11))
print(Solution.longestDiverseString(a=1, b=1, c=7))
print(Solution.longestDiverseString(a=7, b=1, c=0))
