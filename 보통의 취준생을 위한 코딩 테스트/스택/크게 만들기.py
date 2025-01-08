n, k = map(int, input().split())
m = list(input())
# n = 4
# k = 2
cnt = 2
# m = [1, 9, 4, 2]
stack = []


def soultion(n, k):
    for num in range(n):
        while stack and k > 0 and stack[-1] < m[num]:
            del stack[-1]
            k -= 1
        stack.append(m[num])


soultion(n, k)
print("".join(map(str, stack[: n - k])))
