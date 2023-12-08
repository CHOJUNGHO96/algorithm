def solution(경로):
    # 시간초과로 통과못했는데 이유는 최대값과 최솟값의 사이에 모든값을 경로에 대입하여 포함시키는지 확인하기때문에 오래걸린듯함
    정답 = 0
    경로.sort(key=lambda x: x[1])
    경로_최대값 = 경로[-1][-1]
    경로_최솟값 = 경로[0][0]
    임시_dict = {i: [] for i in range(0, len(경로))}

    for 대입값 in range(경로_최솟값, 경로_최대값 + 1):
        카운트 = 0
        for 인덱스, _경로 in enumerate(경로):
            if _경로[0] <= 대입값 <= _경로[1]:
                임시_dict[인덱스].append(대입값)
                카운트 += 1

    비교값 = []
    for 키, 값 in 임시_dict.items():
        if 키 == 0:
            비교값 = 값
            정답 += 1
        else:
            if max(비교값) in 값:
                pass
            else:
                정답 += 1
                비교값 = 값

    return 정답


def solution1(경로):
    # 경로를 나가는 지점을 기준으로 정렬
    경로.sort(key=lambda x: x[1])
    카메라 = -30001  # 카메라 위치를 최소값보다 낮게 초기화
    정답 = 0

    # [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    for 진입, 진출 in 경로:
        # 현재 카메라 위치가 차량 경로를 커버하지 못하는 경우
        if 카메라 < 진입:
            # 카메라를 차량의 진출 지점에 설치
            카메라 = 진출
            정답 += 1

    return 정답


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
