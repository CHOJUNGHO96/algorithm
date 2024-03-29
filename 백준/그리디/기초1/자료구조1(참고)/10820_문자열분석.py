# 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.
# 대문자 65~90, 소문자 97~122, 공백 32, 숫자판단 isdigit()
while True:
    try:
        s = str(input())
        result = [0, 0, 0, 0]
        for i in s:
            if ord(i) in range(97, 123):
                result[0] += 1
            elif ord(i) in range(65, 91):
                result[1] += 1
            elif i.isdigit():
                result[2] += 1
            elif ord(i) == 32:
                result[3] += 1
        print(" ".join(map(str, result)))
    except EOFError:
        break
