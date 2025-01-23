from typing import List
from itertools import combinations


class Solution:
    # @classmethod
    # def threeSum1(cls, nums: List[int]) -> List[List[int]]:
    #     테스트 = list(combinations(nums, 3))
    #     정답 = [sorted(list(i)) for i in 테스트 if sum(i) == 0]
    #     유니크 = list(set(tuple(x) for x in 정답))
    #     유니크 = [list(x) for x in set(tuple(x) for x in 유니크)]
    #     return 유니크

    # @classmethod
    # def threeSum(cls, nums: List[int]) -> List[List[int]]:
    #     nums = sorted(nums)  # [-4, -1, -1, 0, 1, 2]
    #     len_nums = len(nums)
    #     정답 = []
    #     for 인덱스값 in range(len_nums):
    #         if nums[인덱스값] > 0:
    #             continue
    #
    #         for 시작값 in range(인덱스값 + 1, len_nums):
    #             끝값 = 시작값 + 1
    #             while 끝값 < len_nums:
    #                 기준값 = nums[인덱스값] + nums[시작값] + nums[끝값]
    #
    #                 if 기준값 == 0:
    #                     if sorted([nums[인덱스값], nums[시작값], nums[끝값]]) not in 정답:
    #                         정답.append(sorted([nums[인덱스값], nums[시작값], nums[끝값]]))
    #                     시작값 += 1
    #                 elif 기준값 > 0:
    #                     # 투포인터 알고리즘은 루프가돌수록 값이 커지기 때문에 기준값이 0이 넘으면은 무조건 break
    #                     break
    #
    #                 끝값 += 1
    #
    #     return 정답

    @classmethod
    def threeSum(cls, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # [-4, -1, -1, 0, 1, 2]
        len_nums = len(nums)
        정답 = []

        # 투포인터 알고리즘을 활용해야함
        for 인덱스값 in range(len_nums - 2):
            if 인덱스값 > 0 and nums[인덱스값] == nums[인덱스값 - 1]:
                continue

            # 오름차순 정렬한 상태이므로 nums의 제일 마지막 값 * 2가  제일첫번째의 절대값을 초과하지 못하면 나머지 값들을 대입해도 0을 만들지못하므로 continue 한다.
            if abs(nums[인덱스값]) > nums[-1] * 2:
                continue

            # 정해진값을 구하기위해 계속 증가시키는게 아니라 0을 만드는거기 때문에 양쪽에서 좁히면서 탐색해야함
            시작값 = 인덱스값 + 1
            끝값 = len_nums - 1
            while 시작값 < 끝값:
                기준값 = nums[인덱스값] + nums[시작값] + nums[끝값]

                if 기준값 == 0:
                    정답.append([nums[인덱스값], nums[시작값], nums[끝값]])

                    while 시작값 < 끝값 and nums[시작값] == nums[시작값 + 1]:
                        시작값 += 1

                    while 시작값 < 끝값 and nums[끝값] == nums[끝값 - 1]:
                        끝값 -= 1

                    시작값 += 1
                    끝값 -= 1

                if 기준값 > 0:
                    끝값 -= 1
                elif 기준값 < 0:
                    시작값 += 1

        return 정답


print(Solution.threeSum([0, 0, 0, 0]))
print(Solution.threeSum([0, 0, 0]))
print(Solution.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
print(Solution.threeSum([-2, 0, 1, 1, 2]))  # [[-2,0,2],[-2,1,1]]
print(Solution.threeSum([-1, 0, 1, 2, -1, -4]))
