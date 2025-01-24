def solution(answers):
    one_answer = [1, 2, 3, 4, 5]
    two_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    three_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    # 일정한 패턴이있는 리스트(수포자가 찍은문제답)에 인덱스가같은 문제(리스트)의 답을 비교하려면은 패턴리스트[문제 인덱스 % 패턴리스트(수포자가 찍은문제답)] 를 해주면
    # 수포자가 찍은문제답과 맵핑이가능하다
    # ex) 0%5=0, 1%5=1, 2%5=2, 3%5=3, 4%5=4, 5%5=0, 6%5=1, 7%5=2, 8%5=3 ...
    for idx, value in enumerate(answers):
        score[0] += 1 if value == one_answer[idx % len(one_answer)] else 0
        score[1] += 1 if value == two_answer[idx % len(two_answer)] else 0
        score[2] += 1 if value == three_answer[idx % len(three_answer)] else 0

    max_result = max(score)

    result = []
    for idx, value in enumerate(score):
        if value == max_result:
            result.append(idx + 1)

    return result


_answers = [1, 3, 2, 4, 2]
print(solution(_answers))
