def solution(단어: str) -> int:
    import string

    정답 = 0
    플러스_알파벳 = list(string.ascii_uppercase[1:13])
    마이너스_알파벳 = sorted(list(string.ascii_uppercase[13:]), reverse=True)
    인덱스 = 0

    단어 = list(단어)
    while True:

        # 현위치에서 알파벳 변경
        if 단어[인덱스] in 플러스_알파벳:
            정답 += 플러스_알파벳.index(단어[인덱스]) + 1
            단어[인덱스] = "A"
        elif 단어[인덱스] in 마이너스_알파벳:
            정답 += 마이너스_알파벳.index(단어[인덱스]) + 1
            단어[인덱스] = "A"

        # 모든 알파벳이 A로 되었는지 확인
        if 단어 == list("A" * len(단어)):
            return 정답

        # 커서 이동을 위한 변수 설정
        왼쪽, 오른쪽 = 1, 1

        # 커서를 왼쪽으로 움직이는 경우
        while 단어[인덱스 - 왼쪽] == "A":
            왼쪽 += 1

        # 커서를 오른쪽으로 움직이는 경우
        while 단어[인덱스 + 오른쪽] == "A":
            오른쪽 += 1

        # 왼쪽과 오른쪽 중 어디로 움직이는 것이 더 효율적인지 판단
        if 왼쪽 < 오른쪽:
            정답 += 왼쪽
            인덱스 -= 왼쪽
        else:
            정답 += 오른쪽
            인덱스 += 오른쪽


def solution1(알파벳: str) -> int:
    # 초기 조작 횟수를 0으로 설정
    정답 = 0

    # 알파벳 변경을 위한 최소 이동 횟수 계산(아스키코드활용)
    최소알파벳수 = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in 알파벳]

    인덱스 = 0

    while True:
        # 현재 커서 위치에서 알파벳을 목표 알파벳으로 변경
        정답 += 최소알파벳수[인덱스]

        # 변경이 완료되면 0으로 표시
        최소알파벳수[인덱스] = 0

        # 모든 알파벳이 A로 되었는지 확인
        if sum(최소알파벳수) == 0:
            return 정답

        # 커서 이동을 위한 변수 설정
        왼쪽, 오른쪽 = 1, 1

        # 커서를 왼쪽으로 움직이는 경우
        while 최소알파벳수[인덱스 - 왼쪽] == 0:
            왼쪽 += 1

        # 커서를 오른쪽으로 움직이는 경우
        while 최소알파벳수[인덱스 + 오른쪽] == 0:
            오른쪽 += 1

        # 왼쪽과 오른쪽 중 어디로 움직이는 것이 더 효율적인지 판단
        if 왼쪽 < 오른쪽:
            정답 += 왼쪽
            인덱스 -= 왼쪽
        else:
            정답 += 오른쪽
            인덱스 += 오른쪽


# print(solution("AAAAAA"))  # 0
# print(solution("AAAACB"))  # 5
# print(solution("AABAAAAAAABBB"))  # 11
print(solution("CANAAAAANAN"))  # 48
# print(solution("ABAAAAABAB"))  # 8
# print(solution("BBBAAB"))  # 9
# print(solution("CAAAAAA"))  # 2
