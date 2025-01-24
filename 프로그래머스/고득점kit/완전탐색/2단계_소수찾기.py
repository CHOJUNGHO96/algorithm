import math

# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(numbers: str) -> int:
    answer = set()
    numbers = list(numbers)

    def permute(i, data):
        if i == len(data):
            tmp = int("".join(map(str, data)))
            if is_prime_number(tmp):
                answer.add(tmp)
            return

        for j in range(i, len(numbers)):
            if int(data[j]) > 1 and is_prime_number(int(data[j])):
                answer.add(int(data[j]))
            data[i], data[j] = data[j], data[i]
            permute(i + 1, data)
            data[i], data[j] = data[j], data[i]

    permute(0, numbers)
    print(set(answer))
    return len(set(answer))


_numbers = "011"
print(solution(_numbers))
