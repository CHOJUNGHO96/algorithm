from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        메모리_배열 = [[] for _ in range(target + 1)]
        for 요소 in candidates:
            for 인덱스 in range(2, target + 1):
                # 매모리_배열의 각인덱스에 요소를 대입한다
                if len([요소] * (인덱스 // 요소)) < 150:
                    메모리_배열[인덱스].append([요소] * (인덱스 // 요소))
            ...


a = Solution()
print(a.combinationSum([2, 3, 6, 7], 7))
print(a.combinationSum([2, 3, 5], 8))
print(a.combinationSum([2], 1))
