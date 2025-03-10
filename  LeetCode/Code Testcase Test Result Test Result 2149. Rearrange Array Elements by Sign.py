from typing import List
from collections import deque


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        plus_list = deque([])
        minus_list = deque([])
        result = []
        for i in range(len(nums)):
            if len(result) == 0 and nums[i] > 0:
                result.append(nums[i])
                continue
            elif len(result) == 0 and nums[i] < 0:
                minus_list.append(nums[i])
                continue

            if result[-1] > 0 and nums[i] > 0:
                if len(minus_list) > 0:
                    result.append(minus_list.popleft())
                else:
                    plus_list.append(nums[i])
            elif result[-1] < 0 and nums[i] < 0:
                if len(plus_list) > 0:
                    result.append(plus_list.popleft())
                else:
                    minus_list.append(nums[i])

        return result


a = Solution()
print(a.rearrangeArray(nums=[-2, -5, 1, 3, 2, -4]))
print(a.rearrangeArray(nums=[3, 1, -2, -5, 2, -4]))
print(a.rearrangeArray(nums=[-1, 1]))
