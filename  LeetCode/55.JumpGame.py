from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        DFS 이용해서 풀어야함
        """
        arr = [[] for _ in range(len(nums) - 1)]  # [[3, 1], [1, 1, 4], [1], [4]]
        for i in range(len(nums) - 1):
            arr[i] = nums[i + 1 : nums[i] + i + 1]

        def backtracking():
            

        backtracking()
        ...


a = Solution()
# print(a.canJump([0, 2, 3]))
# print(a.canJump([0]))
print(a.canJump([2, 3, 1, 1, 4]))
print(a.canJump([3, 2, 1, 0, 4]))
