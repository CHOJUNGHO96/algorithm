"""
풀이팁
1. 회전을 하는경우가 있으므로 각인덱스의 제일큰수를 가로로 두고 제일작은수중에 제일큰값을 세로로 둔다.
"""

# 나의풀이
def solution(sizes: list) -> int:
    max_w = 0
    max_h = 0
    for i in sizes:
        max_w = max(max_w, max(i))
        max_h = max(max_h, min(i))
    return max_w * max_h


_sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(_sizes))


# 다른사람풀이
def solution1(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


# 다른사람풀이2
solution2 = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
print(solution2(_sizes))
