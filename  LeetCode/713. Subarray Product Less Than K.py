from typing import List
import math


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        current_sum = 1
        left = 0
        result = 0
        for right in range(len(nums)):
            current_sum *= nums[right]
            while current_sum >= k and left <= right:
                current_sum //= nums[left]
                left += 1
            result += right - left + 1
        return result if result > 0 else 0


a = Solution()
print(a.numSubarrayProductLessThanK([1, 2, 3, 4, 5], 1))
print(a.numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))
print(a.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(a.numSubarrayProductLessThanK([1, 2, 3], 0))
