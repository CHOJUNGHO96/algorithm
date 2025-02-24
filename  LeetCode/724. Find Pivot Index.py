from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum1 = [0]
        prefix_sum2 = [0]
        for idx in range(len(nums)):
            prefix_sum1[idx] = prefix_sum1[idx - 1] + nums[idx]
            prefix_sum2[idx] = prefix_sum2[idx - 1] + nums[-idx]

        prefix_sum1


a = Solution()
print(a.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(a.pivotIndex(nums=[1, 2, 3]))
print(a.pivotIndex(nums=[2, 1, -1]))
