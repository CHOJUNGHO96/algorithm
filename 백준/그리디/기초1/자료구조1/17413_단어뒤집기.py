"""
문제
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.

먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
문자열의 시작과 끝은 공백이 아니다.
'<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다. 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

입력
첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.

출력
첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.

예제 입력 1
baekjoon online judge
예제 출력 1
noojkeab enilno egduj

예제 입력 2
<open>tag<close>
예제 출력 2
<open>gat<close>

예제 입력 3
<ab cd>ef gh<ij kl>
예제 출력 3
<ab cd>fe hg<ij kl>

예제 입력 4
one1 two2 three3 4fourr 5five 6six
예제 출력 4
1eno 2owt 3eerht rruof4 evif5 xis6

예제 입력 5
<int><max>2147483647<long long><max>9223372036854775807
예제 출력 5
<int><max>7463847412<long long><max>7085774586302733229
"""
from collections import deque

단어 = input()
정답 = ""
체크 = False
임시큐 = deque()

for i in 단어:
    # "<" 일때 임시큐에 담아뒀던 단어들을 정답에 거꾸로 넣어주고 체크플래그 활성화
    if i == "<":
        체크 = True
        임시큐.appendleft(i)
        for _ in range(0, len(임시큐)):
            정답 += 임시큐.pop()

    # ">" 임시큐에 담아뒀던 단어들을 정답에 순서대로 넣어준다 체크플래그 비활성화
    elif i == ">":
        체크 = False
        임시큐.append(i)
        for _ in range(0, len(임시큐)):
            정답 += 임시큐.popleft()

    # 띄어쓰기이고 체크플래그 비활성화일경우 임시큐에 담아뒀던 단어들을 정답에 거꾸로 넣어준다
    elif i == " " and not 체크:
        for _ in range(0, len(임시큐)):
            정답 += 임시큐.pop()
        정답 += " "
    else:
        임시큐.append(i)

# for루프가 끝나고 임시큐에 단어가 남아있으면 정답에 거꾸로 넣어준다
else:
    for _ in range(0, len(임시큐)):
        정답 += 임시큐.pop()

print(정답)


# 스택을 이용한 풀이 (다른사람)
data = input()

stack = []
ans = ""
check = False  # 괄호안의 여부를 체크
for d in data:
    # 스택에 존재하는 값을 역으로 추가합니다.
    if d == "<":
        check = True
        for _ in range(len(stack)):
            ans += stack.pop()

    stack.append(d)
    # 스택에 존재하는 값은 괄호안의 값이기에 순차적으로 추가합니다.
    if d == ">":
        check = False
        for _ in range(len(stack)):
            ans += stack.pop(0)  # pop(0)을하면 맨처음에있는 요소가 pop이된다 큐의 popleft와 동일
    # 스택에 존재하는 값을 역으로 추가합니다.
    if d == " " and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            ans += stack.pop()
        ans += " "
# 스택에 값이 남아있는 경우는 괄호의 경우가 아니기에 역으로 추가합니다.
if stack:
    for _ in range(len(stack)):
        ans += stack.pop()

print(ans)
