from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_value = max(nums)
        result = 0
        k_count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == max_value:
                k_count += 1
            while k_count >= k:
                result += len(nums) - right
                if nums[left] != max_value:
                    left += 1
                elif nums[left] == max_value:
                    k_count -= 1
                    left += 1

        return result


a = Solution()
print(a.countSubarrays(nums=[28, 5, 58, 91, 24, 91, 53, 9, 48, 85, 16, 70, 91, 91, 47, 91, 61, 4, 54, 61, 49], k=1))
print(
    a.countSubarrays(
        nums=[2, 2, 2, 2, 1, 3, 3, 2, 2, 1, 1, 3, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 3], k=5
    )
)
print(a.countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
print(a.countSubarrays(nums=[1, 4, 2, 1], k=3))
