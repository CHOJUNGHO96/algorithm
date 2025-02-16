from typing import List

"""
1. 수학적 개념
우리가 부분 배열의 합을 구할 때, 두 인덱스 i, j(i ≤ j) 사이의 합은 누적합을 이용하면 다음과 같이 표현 가능:
sum(i,j) = prefixSum[j] − prefixSum[i−1]
즉, prefixSum[j]는 0번부터 j번까지의 누적합, prefixSum[i-1]은 0번부터 i-1번까지의 누적합.
이제 우리가 원하는 것은 어떤 부분합 sum(i, j)가 k가 되는 경우를 찾는 것.
prefixSum[j] − prefixSum[i−1] = k
prefixSum[𝑖−1] = prefixSum[𝑗] − 𝑘
prefixSum[i−1] = prefixSum[j] − k
즉, prefixSum[j] - k 값이 기존의 prefixSum[i-1] 중에 존재한다면, 해당 부분배열이 조건을 만족하는 것!

2. 해시맵(HashMap) 활용
위 수식을 활용하기 위해, prefixSum[j] 값을 계산하면서, prefixSum[i-1] = prefixSum[j] - k 가 존재하는지를 빠르게 찾으면 됨. 
여기서 해시맵(딕셔너리)를 이용하면 O(1) 시간 안에 해당 값이 존재하는지를 확인 가능

알고리즘 흐름
누적합을 계산하면서
prefixSum[j] - k가 prefixSum 기록된 값에 존재하는지 확인
존재한다면 해당 prefixSum[i-1]가 prefixSum[j] - k와 같은 값이므로 조건 만족하는 부분 배열 개수를 더함
현재 prefixSum[j]를 해시맵에 저장하여 이후 탐색에 활용
"""


class Solution:
    """
    nums가 1, 2, 1, 3 이고 들어오고 k가 3인경우
    1. 중첩해서 더해주는 값을 해쉬테이블에 저장 {0,1,3,4,7} 0을 넣어주는 이유는 2번에서 설명한다
    2. 3을 더해야하는 경우의 수를 구한다 (0 -> 3), (1 -> 4), (4 -> 7) 해쉬테이블에 0을 안넣어줬으면 3은 포함이 안되니깐 넣어준거다.
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = {0: 1}
        prefix_sum = 0
        result = 0
        for value in nums:
            prefix_sum += value
            if prefix_sum - k in hash_table:
                result += hash_table[prefix_sum - k]
            hash_table[prefix_sum] = hash_table.get(prefix_sum, 0) + 1
        return result


a = Solution()
print(a.subarraySum([1, 1, 1], 2))
print(a.subarraySum([1, 2, 3], 3))
print(a.subarraySum([1, 2, 1, 3], 3))
print(a.subarraySum([3, 4, 7, -2, 2, 1, 4, 2], 7))
