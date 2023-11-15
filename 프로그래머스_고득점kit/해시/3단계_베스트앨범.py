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

    # 인덱스와 재생횟수를 결합하기위한작업
    # ex : [[0, 500], [1, 600], [2, 150], [3, 800], [4, 2500]]
    재생횟수 = [[인덱스, 값] for 인덱스, 값 in enumerate(재생횟수)]

    # 노래장르에속한 재생횟수에대한 dict 를 만들어준다
    # ex : {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]}
    for 장르, 횟수 in zip(노래장르, 재생횟수):
        if 장르 not in 임시_dic:
            임시_dic[장르] = []
        임시_dic[장르].append(횟수)

    # 장르와 장르에해당한 재생횟수의 총합을 묶기위한 list
    임시_list = []

    for 장르, 횟수 in 임시_dic.items():
        # 장르에 속한 노래중 재생횟수가 많은순서대로 정렬
        # ex :{'classic': [0, 500], [2, 150]], [[3, 800]} --> {'classic': [[3, 800], [0, 500], [2, 150]]}
        횟수.sort(key=lambda x: x[1], reverse=True)

        # 장르에속한 재생횟수의 총합을구하여 임시_list에 장르와 총합을 묶어서 append
        # [['classic', 1450], ['pop', 3100]]
        총합 = sum([i[1] for i in 횟수])
        임시_list.append([장르, 총합])

        # 총합을 다구했으므로 배스트앨범2개까지만 남긴다
        # ex : {'classic': [[3, 800], [0, 500]]}
        if len(횟수) > 2:
            임시_dic[장르] = 횟수[:2]

    # 재생횟수가 가장많은 장르순으로 정렬
    # ex : [['classic', 1450], ['pop', 3100]] --> [['pop', 3100], ['classic', 1450]]
    임시_list.sort(key=lambda x: x[1], reverse=True)

    # 정답에 정렬된 장르순으로 장르에속한 앨범들을 넣어준다
    for 값 in 임시_list:
        정답 += [i[0] for i in 임시_dic[값[0]]]

    return 정답


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(
    solution(
        ["jazz", "rap", "hiphop", "jazz", "jazz", "hiphop"],
        [100, 1000, 50, 100, 50, 500],
    )
)
