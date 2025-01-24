import math


def solution(progresses, speeds):
    answer = []
    tmp = 0
    cnt = 0
    for p, s in zip(progresses, speeds):
        if tmp == 0:
            tmp = math.ceil((100 - p) / s)

        if tmp < math.ceil((100 - p) / s):
            answer.append(cnt)
            cnt = 0
            tmp = math.ceil((100 - p) / s)
        cnt += 1
    else:
        answer.append(cnt)
    return answer


# def solution(progresses, speeds):
#     Q = []
#     for p, s in zip(progresses, speeds):
#         if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
#             Q.append([-((p - 100) // s), 1])
#         else:
#             Q[-1][1] += 1
#     return [q[1] for q in Q]


_progresses = [93, 30, 55]
_speeds = [1, 30, 5]
# _progresses = [95, 90, 99, 99, 80, 99]
# _speeds = [1, 1, 1, 1, 1, 1]
print(solution(_progresses, _speeds))
