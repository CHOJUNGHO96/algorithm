from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        백트래킹 알고리즘으로 탐색을 진행해야함
        """
        result = []

        def backtracking(idx, path, total):
            if total > target:
                return
            if total == target:
                result.append(list(path))
                return
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                backtracking(i, path, total + candidates[i])
                path.pop()

        backtracking(0, [], 0)
        return result


a = Solution()
print(a.combinationSum([2, 3, 6, 7], 7))
print(a.combinationSum([2, 3, 5], 8))
print(a.combinationSum([2], 1))
