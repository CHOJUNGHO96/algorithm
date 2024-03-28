# 입력받은 문자열을 ord를 이용해서 유니코드로변환
# 문자열을 루프돌면서 temp_dict에 맞는곳에 해당 인덱스로 대입
# 처음등장하는 알파벳으로 대입해야함

s = str(input())  # baekjoon
s = [ord(i) for i in s]
temp_dict = {i: -1 for i in range(97, 123)}
temp_list = []

for idx, v in enumerate(s):
    if v not in temp_list:
        temp_dict[v] = idx
        temp_list.append(v)

print(" ".join(map(str, [v for k, v in temp_dict.items()])))


# 다른사람풀이 (find사용)
# find 함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력한다 만일 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력하는 함수이다.
S = input()

for x in "abcdefghijklmnopqrstuvwxyz":
    print(S.find(x), end=" ")
