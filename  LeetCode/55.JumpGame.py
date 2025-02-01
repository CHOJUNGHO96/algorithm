from typing import List


class Solution:
    def canJump1(self, nums):
        n = len(nums)

        def dfs(index):
            if index >= n - 1:
                return True

            max_jump = nums[index]
            for step in range(1, max_jump + 1):
                if dfs(index + step):
                    return True

            return False

        return dfs(0)

    def canJump(self, nums):
        max_reach = 0
        n = len(nums)

        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True

        return False


a = Solution()
# print(a.canJump([0, 2, 3]))
# print(a.canJump([0]))
print(a.canJump([2, 3, 1, 1, 4]))
print(a.canJump([3, 2, 1, 0, 4]))
