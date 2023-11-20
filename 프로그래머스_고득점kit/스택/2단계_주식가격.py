def solution(가격들):
    """
    1. 가격들에있는 가격을 popleft 하여 남아있는 가격들과 비교후 횟수를 올려준다
    2. for 루프가 끝나면 횟수를 정답스택에 append 한다.

    주의
    2중 for문으로 했을때 시관초과 에러가나서 큐를 이용하여 풀어야함
    """
    from collections import deque

    정답 = []
    가격들 = deque(가격들)

    while 가격들:
        타겟_가격 = 가격들.popleft()
        횟수 = 0
        for 가격 in 가격들:
            if 타겟_가격 <= 가격:
                횟수 += 1
            else:
                횟수 += 1
                break
        정답.append(횟수)
    return 정답


print(solution([1, 2, 3, 2, 3]))  # 4, 3, 1, 1, 0
print(solution([3, 1, 2, 2, 3, 1]))  # 1, 4, 3, 2, 1, 0
print(solution([1, 2, 3, 1, 2, 3, 3, 1, 2]))  # 8, 2, 1, 5, 3, 2, 1, 1, 0
