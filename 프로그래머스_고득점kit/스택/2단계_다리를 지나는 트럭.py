def solution(트럭수, 견딜수있는무게, 트럭들):
    """
    주의
    현재무게를 기록하기위해 건널다리에있는 트럭의 무게를합치려고 sum 함수사용했는데 시간초에서 실패함
    sum 함수 사용은 자제하도록하자
    """
    from collections import deque

    초 = 0
    트럭들 = deque(트럭들)

    # 다리를건너는 트럭을위한 건널다리 생성 (빈다리이므로 0으로 세팅한다)
    건널다리 = deque([0] * 트럭수)

    현재무게 = 0
    # 루프로 트럭별 무게에서 하나씩빼고 루프마다 1초씩 경과하고 건널다리가 빌때까지 수행
    while 건널다리:
        초 += 1

        # 먼저 모든 트럭들이 빌때까지 진행
        if len(트럭들) != 0:
            # 트럭 출발시키고 건널다리에있는 트럭들도 출발시켜준다
            # [0,0] -> [0,7] -> [7,0] -> [0,4] -> [4,5] ...
            트럭 = 트럭들.popleft()
            떠나간트럭 = 건널다리.popleft()

            # 출발한 트럭들의 무게를 저장한다.
            현재무게 += 트럭

            # 떠나간 트럭의 무게를 뺀다
            현재무게 -= 떠나간트럭

            # 현재무게가 견딜수있는 무게보다 같거나 적을시 건널다리에 트럭추가
            if 현재무게 <= 견딜수있는무게:
                건널다리.append(트럭)
            else:
                # 건널다리에 있는 트럭무게가 견딜수있는무게를 초과할경우 처음에 건널다리에 popleft 한거를 매꾸기위해 0을 추가
                건널다리.append(0)
                # 출발한 트럭을다시 처음순번으로 대기
                트럭들.appendleft(트럭)
                현재무게 -= 트럭
        else:
            # 모든 트럭들은 출발을했으면 건널다리에있는 남은 트럭들을 움직여준다
            건널다리.popleft()

    return 초


print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(3, 10, [7, 4, 5, 6]))  # 11
print(solution(2, 10, [4, 5, 4, 6]))  # 6
print(solution(2, 10, [7, 4, 5, 4, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
print(solution(1, 2, [1, 1, 1]))  # 4
print(solution(1, 1, [1, 1, 1]))  # 4
print(solution(4, 2, [1, 1, 1, 1]))  # 10
print(solution(3, 3, [1, 1, 1]))  # 6
print(solution(3, 1, [1, 1, 1]))  # 10
print(solution(3, 1, [1, 1, 1, 1, 1]))  # 16
print(solution(5, 5, [1, 1, 1, 1, 1, 2, 2]))  # 14
print(solution(7, 7, [1, 1, 1, 1, 1, 3, 3]))  # 18
print(solution(5, 5, [1, 1, 1, 1, 1, 2, 2, 2, 2]))  # 19
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))  # 19
