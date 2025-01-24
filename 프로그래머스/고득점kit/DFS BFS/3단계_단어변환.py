def solution1(시작단어, 타겟단어, 단어들):
    """
    주의
    1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
    2. 단어들에 있는 단어로만 변환할 수 있습니다.
    """
    from collections import deque

    정답 = 0

    # 중복된 단어가 있을수있으므로 중복제거
    단어들 = list(set(단어들))

    # 단어들에 타겟단어가 없으면 0리턴
    if 타겟단어 not in 단어들:
        return 정답

    # 큐를 이용하여 알고리즘을 진행하기위한 세팅
    단어들 = deque(단어들)
    대상큐 = deque()

    # 단어들이 빌때까지 루프수행
    while 단어들:
        # 글자가 2개부터 동일하지않으면 변경할수 없는글자임을 알려주는 카운트값
        cnt = 0

        # 처음에는 대상큐가 비어있으므로 단어들안에 시작단어에서 변경할수있는 단어를찾아 대상큐에 넣어준다.
        if len(대상큐) == 0:
            단어 = 단어들.popleft()

            # 단어들에서 popleft한 단어중 시작단어와 단어가 1개만틀린 단어들을 대상큐에 넣는거나 바로 타겟단어로 변경할수있는지 체크하는 로직
            for 시작글자, 단어글자 in zip(시작단어, 단어):

                # 글자가 틀리면 cnt값 증가
                if 시작글자 != 단어글자:
                    cnt += 1

                # cnt가 2면은 글자수가 2개이상 불일치하므로 해당 단어는 맨마지막순으로 단어들에 appned 시킨다
                if cnt == 2:
                    단어들.append(단어)
                    break

            # 위의 로직에서 안맞는글자수가 2개 미만으로 있을경우 정답을 + 1해주고 대상큐에 해당 단어를 넣어주거나 타겟단어와 같으면 return 해준다.
            else:
                정답 += 1
                if 단어 == 타겟단어:
                    return 정답
                대상큐.appendleft(단어)

        # 위와 동일하게 큐에있는 단어들을 하나씩 빼서 남아있는 단어들과 매칭
        if 대상큐:
            cnt = 0
            대상큐_단어 = 대상큐.popleft()
            단어 = 단어들.popleft()

            for 대상큐_글자, 단어글자 in zip(대상큐_단어, 단어):
                if 대상큐_글자 != 단어글자:
                    cnt += 1
                if cnt == 2:
                    if len(단어들) != 0:
                        단어들.append(단어)
                        대상큐.appendleft(대상큐_단어)
                    break
            else:
                정답 += 1
                cnt = 0
                for 대상큐_글자, 단어글자 in zip(대상큐_단어, 타겟단어):
                    if 대상큐_글자 != 단어글자:
                        cnt += 1
                    if cnt > 1:
                        break
                else:
                    return 정답

                if 단어 == 타겟단어:
                    return 정답
                대상큐.appendleft(단어)
    return 0


from collections import deque


def 단어체크(단어1, 단어2):
    # 두 단어 사이에 한 글자만 다른지 확인
    틀린횟수 = 0
    for c1, c2 in zip(단어1, 단어2):
        if c1 != c2:
            틀린횟수 += 1
        if 틀린횟수 > 1:
            return False
    return 틀린횟수 == 1


def solution(시작단어, 타겟단어, 단어들):
    """
    bfs 풀이
    """

    # 타겟단어가 단어들에 포함없으면 리턴
    if 타겟단어 not in 단어들:
        return 0

    방문체크 = set()

    # 큐에 조사할 단어와 변환 횟수를 같이 기록해둔다
    큐 = deque([(시작단어, 0)])  # (현재 단어, 변환 횟수)

    while 큐:
        큐단어, 변환횟수 = 큐.popleft()
        if 큐단어 == 타겟단어:
            return 변환횟수

        for 단어 in 단어들:
            if 단어 not in 방문체크 and 단어체크(큐단어, 단어):
                방문체크.add(단어)
                큐.append((단어, 변환횟수 + 1))

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "fog", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]))  # 1
print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"]))  # 3
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]))  # 4
print(solution("hit", "bak", ["hot", "dot", "dog", "lot", "log", "bak"]))  # 0
print(solution("hit", "hhh", ["hhh", "hht"]))  # 2
print(solution("hit", "bak", ["hot", "dot", "dog", "lot", "log", "bak"]))  # 0
print(solution("hit", "hhh", ["hhh", "hht"]))  # 2
print(solution("hit", "gga", ["hot", "dot", "dog", "lot", "log", "cog", "gga"]))  # 0
