def solution(노래장르, 재생횟수):
    """
    수록기준
    1. 장르가제일많은걸 먼저
    2. 장르내 많이 재생된 노래먼저
    3. 재생횟수가 같으면 고유번호가 낮은 노래먼저

    주의
    1. 최대 2개까지의 베스트앨범을 낸다.
    """
    정답 = []
    임시_dic = {}
    재생횟수 = [[인덱스, 값] for 인덱스, 값 in enumerate(재생횟수)]

    for 장르, 횟수 in zip(노래장르, 재생횟수):
        if 장르 not in 임시_dic:
            임시_dic[장르] = []
        임시_dic[장르].append(횟수)

    임시_list = []
    for 장르, 횟수 in 임시_dic.items():
        횟수.sort(key=lambda x: x[1], reverse=True)

        총합 = sum([i[1] for i in 횟수])
        임시_list.append([장르, 총합])
        if len(횟수) > 2:
            횟수.pop()
    임시_list.sort(key=lambda x: x[1], reverse=True)

    for 값 in 임시_list:
        정답 += [i[0] for i in 임시_dic[값[0]]]

    return 정답


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    )
)
print(
    solution(
        ["jazz", "rap", "hiphop", "jazz", "jazz", "hiphop"],
        [100, 1000, 50, 100, 50, 500],
    )
)
