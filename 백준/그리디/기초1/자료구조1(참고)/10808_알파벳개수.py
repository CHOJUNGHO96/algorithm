s = str(input())
# a~z 까지의 딕셔너리를 만든다 유니코드로 97~122
temp_dict = {i: 0 for i in range(97, 123)}

# s를 각각유니코드리스트로 변환한다
s = [ord(i) for i in s]

for i in s:
    temp_dict[i] += 1
print(" ".join(map(str, [v for k, v in temp_dict.items()])))
