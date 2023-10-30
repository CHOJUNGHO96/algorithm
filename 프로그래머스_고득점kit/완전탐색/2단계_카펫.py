def solution(갈색, 노란색):
    # 전체 격자의 수
    total = 갈색 + 노란색

    # 가로, 세로 길이를 찾기
    # 제곱근의 원리를위해 total + 1 가 아닌 int(total**0.5) + 1 로 해준다
    for i in range(1, int(total**0.5) + 1):
        if total % i == 0:
            j = total // i
            # 테두리에는 갈색 격자가 있으므로 (가로 - 2) * (세로 - 2) = 노란색 격자의 수
            """
            아래처럼 존재할경우 노란색은 가로 3(5 - 2)과 세로 2(4 - 2)로 구성되어 있으므로    
갈 갈 갈 갈 갈
갈 노 노 노 갈
갈 노 노 노 갈
갈 갈 갈 갈 갈            
            """
            if (i - 2) * (j - 2) == 노란색:
                return [j, i]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
