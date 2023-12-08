임시답 = 0


def solution(단어):
    def DFS(비교대상_단어, _단어):
        # DFS 탐색할때마다 탐색횟수를 늘려주면서 원하는 단어가 나올때까지 탐색을 진행
        # ex: A = 1, AA = 2, AAA = 3, AAAA = 4 , AAAAA = 5, AAAAE = 6, AAAAI = 7, AAAAO = 8 AAAAU = 9, AAAAE = 10 ...

        _기준단어 = ["A", "E", "I", "O", "U"]
        global 임시답
        임시답 += 1

        # 탐색한 단어가 예시 단어와 맞으면 리턴
        if 비교대상_단어 == _단어:
            return True

        # 단어 길이제한은 5임
        if len(비교대상_단어) == 5:
            return False

        # DFS 탐색이므로 AAAAA 까지 탐색하면 재귀로 AAAAE 로탐색
        for 글자 in _기준단어:
            if DFS(비교대상_단어 + 글자, _단어):
                return True

    기준단어 = ["A", "E", "I", "O", "U"]
    for a in 기준단어:
        if DFS(a, 단어):
            global 임시답
            정답 = 임시답
            임시답 = 0
            return 정답


# 다른사람풀이
def solution2(word):
    answer = 0
    dic = ["A", "E", "I", "O", "U"]
    li = [5**i for i in range(len(dic))]

    for i in range(len(word) - 1, -1, -1):
        idx = dic.index(word[i])
        for j in range(5 - i):
            answer += li[j] * idx
        answer += 1
    return answer


# 다른사람풀이
def solution3(word):
    from itertools import product

    answer = []
    li = ["A", "E", "I", "O", "U"]
    for i in range(1, 6):
        for per in product(li, repeat=i):
            answer.append("".join(per))
    answer.sort()
    return answer.index(word) + 1


print(solution("AAAAE"))  # 6
print(solution("AAAE"))  # 10
print(solution("I"))  # 1563
print(solution("EIO"))  # 1189
