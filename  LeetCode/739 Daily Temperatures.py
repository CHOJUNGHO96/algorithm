from typing import List
from collections import deque
import copy


class Solution:
    @classmethod
    def dailyTemperatures1(cls, temperatures: List[int]) -> List[int]:
        # 정렬시킨후에 소거 [73,74,75,71,69,72,76,73], [(73, 0), (74, 1), (75, 2), (71, 3), (69, 4), (72, 5), (76, 6), (73, 7)]
        # [69, 71, 72, 73, 73, 74, 75, 76, 77, 78]
        tmp_temperatures = deque()
        for idx, i in enumerate(temperatures):
            tmp_temperatures.append((i, idx))
        print(tmp_temperatures)

        result = []
        for _ in temperatures:
            pop_left_data = (
                tmp_temperatures.popleft()
            )  # [(73, 0), (74, 1), (75, 2), (71, 3), (69, 4), (72, 5), (76, 6), (73, 7)]
            copy_temperatures = copy.deepcopy(sorted(tmp_temperatures))
            min = 0
            max = len(copy_temperatures)
            tmp_result = 0
            while min < max:
                standard_len = (min + max) // 2
                temper = copy_temperatures[standard_len][0]
                if temper <= pop_left_data[0] and pop_left_data[1] < copy_temperatures[standard_len][1]:
                    min = standard_len + 1
                elif temper > pop_left_data[0]:
                    max = standard_len
                    tmp_result = copy_temperatures[standard_len]
            else:
                result.append(tmp_result[1] - pop_left_data[1])

    ...

    @classmethod
    def dailyTemperatures2(cls, 온도리스트: List[int]) -> List[int]:
        답 = []
        for 인덱스, 온도 in enumerate(온도리스트):
            count = 0
            정답길이 = len(답)
            if 인덱스 == len(온도리스트):
                답.append(0)
            for _온도 in 온도리스트[인덱스 + 1 : len(온도리스트)]:
                count += 1
                if 온도 < _온도:
                    답.append(count)
                    break
            else:
                if 정답길이 == len(답):
                    답.append(0)

        return 답

    @classmethod
    def dailyTemperatures(cls, 온도리스트: List[int]) -> List[int]:
        답 = [0] * len(온도리스트)
        스택 = []

        for 현재인덱스, 현재온도 in enumerate(온도리스트):
            while 스택 and 현재온도 > 온도리스트[스택[-1]]:
                이전인덱스 = 스택.pop()
                답[이전인덱스] = 현재인덱스 - 이전인덱스
            스택.append(현재인덱스)

        return 답


print(Solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(Solution.dailyTemperatures([30, 40, 50, 60]))
print(Solution.dailyTemperatures([30, 60, 90]))
