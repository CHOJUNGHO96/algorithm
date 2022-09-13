"""
문제
국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다.
그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고
그 합이 484로 가능한 최대가 된다.

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

입력
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다.
다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다.
그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다.

출력
첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.

예제 입력 1
4
120 110 140 150
485
예제 출력 1
127

예제 입력 2
5
70 80 30 40 100
450
예제 출력 2
100
"""

# 입력
n = int(input())
requests = list(map(int, input().split()))
budget = int(input())

low = 0
high = max(requests)
upper_limit = -1


# 상한액 구하는 함수
def calculate_needed_budget(mid_val: int) -> int:
    need_value = 0
    # 상한액과 각지방의 예산액중 최소값을 기준으로 더한다. (각지방 예산이 상한액보다 클이유가 없기때문)
    for request_val in requests:
        need_value += min(request_val, mid_val)
    return need_value


while low <= high:
    mid = (low + high) // 2
    # mid 값으로 합친게 budget 보다 작으면 low가 mid + 1로 바껴야함
    # mid 가 75 이여서 300 <= 450 일경우 75보다 작은수는 필요없으므로 low가 75 + 1로적용
    if calculate_needed_budget(mid) <= budget:
        upper_limit = mid
        low = mid + 1
    # mid 값으로 합친게 budget 보다 크면 high가 mid - 1로 바껴야함
    # mid 가 150 이여서 600 >= 450 일경우 150보다 큰수는  필요없으므로 high가 150 - 1로 적용
    else:
        high = mid - 1
print(upper_limit)

# 배정된 예산들 중 최댓값인 정수를 출력하기
# 각지방 예산과 상한액중 최소값을 min_val 에 세팅후 max_upper_limit 에 초기화시킨뒤 루프를 통해 max(max_upper_limit, min_val) 로 예산들중 최대값 정수 찾기
# max_upper_limit = -1
# for request_val in requests:
#     min_val = min(request_val, upper_limit)
#     max_upper_limit = max(max_upper_limit, min_val)
# print(max_upper_limit)
