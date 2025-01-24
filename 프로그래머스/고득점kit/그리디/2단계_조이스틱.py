def solution(단어):
    """
    1. 알파벳 변경한값저장
    2. 위치 변경
    """
    정답 = 0

    # 처음 최소이동거리는 단어의 길이 - 1로세팅한다
    최소이동거리 = len(단어) - 1
    for 인덱스, 알파벳 in enumerate(단어):
        # 해당알파벳을 위, 아래로 움직인 경우의 최솟값을 정답에 넣어준다
        정답 += min(ord(알파벳) - ord("A"), ord("Z") - ord(알파벳) + 1)

        # next 세팅은 처음위치에서 알파벳까지의 이동으로 세팅
        next = 인덱스 + 1

        # 알파벳 이후의 연속된 A의 값찾기
        while next < len(단어) and 단어[next] == "A":
            next += 1

        """        
        2번 (2 * 인덱스) + len(단어) - next : 오른쪽으로 알파벳만큼갔다가 다시 원복후 왼쪽으로 이동
        ex : BBBBAABB 인경우 연속된 A전까지 3번을 갔다가 원복하므로 (3*2) 한후 왼쪽으로 이동해야하므로 (len(단어) - next(연속된A까지의 인덱스포함임))
        
        3번 인덱스 + 2 * (len(단어) - next) : 왼쪽으로 알파벳만큼 갓다가 원복후 오른쪽으로 이동
        ex : BBBBAABB 인경우 왼쪽으로 연속된 A까지 왕복한값이므로 (len(단어) - next(연속된A까지의 인덱스포함임))에 오른쪽으로 해당 인덱스까지더한값 
        """

        최소이동거리 = min(최소이동거리, (2 * 인덱스) + len(단어) - next, 인덱스 + 2 * (len(단어) - next))
    return 정답 + 최소이동거리


# print(solution("AAAAAA"))  # 0
# print(solution("AAAACB"))  # 5
print(solution("BBBBAABB"))  # 11
# print(solution("AABAAAAAAABBB"))  # 11
# print(solution("AABAAAAABBBAAAAAAABA"))  # 11
# print(solution("CANAAAAANAN"))  # 48
# print(solution("ABAAAAABAB"))  # 8
# print(solution("BBBAAB"))  # 9
# print(solution("CAAAAAA"))  # 2
