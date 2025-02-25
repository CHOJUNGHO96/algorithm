from typing import List


class Solution:
    """
    nums=[1, 7, 3, 6, 5, 6] 의 prefix_sum이 [0,1,8,11,17,22,28] 일때 17기준으로 왼쪽합이 11 이고 오른쪽합이 11이여서 17의 인덱스 3이 반환이 되는거다.
    문제의 핵심은 현재 피벗 왼쪽의합이 오른쪽합과 똑같다는 가정이면 prefix_sum[i-1] == sum(nums) - prefix_sum[i] 가 성립이된다.
    """

    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        sum_value = sum(nums)
        for idx in range(1, len(nums) + 1):
            prefix_sum.append(prefix_sum[idx - 1] + nums[idx - 1])
            if sum_value - prefix_sum[idx] == prefix_sum[idx - 1]:
                return idx - 1

        return -1


a = Solution()
print(a.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(a.pivotIndex(nums=[1, 2, 3]))
print(a.pivotIndex(nums=[2, 1, -1]))
