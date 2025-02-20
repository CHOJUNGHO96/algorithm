from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0  # goal이 음수면 존재할 수 없음
            left = count = sum_ = 0
            for right in range(len(nums)):
                sum_ += nums[right]
                while sum_ > k:  # sum이 k보다 크면 왼쪽 포인터 이동
                    sum_ -= nums[left]
                    left += 1
                count += right - left + 1  # 현재 윈도우 내의 모든 부분 배열 개수 추가
            return count

        return atMost(goal) - atMost(goal - 1)


a = Solution()
print(a.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
print(a.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
