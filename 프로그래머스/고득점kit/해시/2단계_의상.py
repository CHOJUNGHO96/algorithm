from collections import defaultdict


def solution(clothes):
    answer = 0

    # 해시로 묶기위한작업
    a = defaultdict(list)
    for i, j in clothes:
        a[j].append(i)

    # 같은종류의 옷을 한번씩 입거나 아예 안입으므로 각 옷종류마다 len(v) + 1 한값을 곱해준다(섞어서 입을수있으므로)
    # EX : headgear의 옷은 2개이므로 한번씩 다입거나 안입는경우는 2+1 이고 나머지 옷종류를 섞어서 조합할수있으므로 곱해준다.
    for k, v in a.items():
        if answer == 0:
            answer = len(v) + 1
        else:
            answer *= len(v) + 1

    # 모든옷을 입지않는 경우를 제외하기위해 -1 해준다
    return answer - 1


def solution(clothes):
    from collections import Counter
    from functools import reduce

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


_clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(_clothes))
