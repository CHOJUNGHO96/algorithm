from typing import List
from collections import deque


class Solution:
    @classmethod
    def largestNumber1(cls, 요소들: List[int]) -> str:
        정답 = []
        if len(요소들) == 2:
            작은_요소 = min(요소들)
            if int(str(요소들[0])[0 : len(str(작은_요소))]) <= int(str(요소들[1])[0 : len(str(작은_요소))]):
                요소들.reverse()

            return f"{str(요소들[0])}{str(요소들[1])}"

        요소들_복제 = [(int(str(요소 * 100000000)[0:9]) + (10 / len(str(요소))), 인덱스) for 인덱스, 요소 in enumerate(요소들)]
        요소들_복제 = deque(sorted(요소들_복제, reverse=True))

        while 요소들_복제:
            요소_인덱스 = 요소들_복제.popleft()
            정답.append(요소들[요소_인덱스[1]])

        return str(int("".join(map(str, 정답))))

    @classmethod
    def largestNumber(cls, 요소들: List[int]) -> str:
        요소들_문자열 = list(map(str, 요소들))

        요소들_문자열.sort(key=lambda x: x * 10, reverse=True)

        정답 = "".join(요소들_문자열)

        return "0" if 정답[0] == "0" else 정답


print(Solution.largestNumber([0, 0, 0]))
print(Solution.largestNumber([111311, 1113]))
print(Solution.largestNumber([10, 2]))
print(Solution.largestNumber([3, 30, 34, 5, 9]))
print(Solution.largestNumber([0, 0, 0, 0, 1]))