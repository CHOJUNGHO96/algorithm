# 내풀이
class Solution:
    # 65~90 대문자, 97~122 소문자
    def reverseOnlyLetters(self, s: str) -> str:
        result = list("a" * (len(s)))
        ascii_code1 = list(range(65, 91))
        ascii_code2 = list(range(97, 123))
        result2 = [i for i in list(s) if ord(i) in ascii_code1 or ord(i) in ascii_code2]
        s = list(s)
        for left in range(len(s)):
            if ord(s[left]) not in ascii_code1 and ord(s[left]) not in ascii_code2:
                result[left] = s[left]
            else:
                result[left] = result2.pop()

        return "".join(result)


# 다른사람 풀이 isalpha 함수를 사용해서 문자열인지 아닌지 확인가능
class Solution2:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        l, r = 0, n - 1
        char_list = [c for c in s]
        while l < r:
            while not char_list[l].isalpha() and l < r:
                l += 1
            while not char_list[r].isalpha() and l < r:
                r -= 1

            char_list[l], char_list[r] = char_list[r], char_list[l]
            l += 1
            r -= 1
        return "".join(char_list)


a = Solution2()
# print(a.reverseOnlyLetters(s="ab-cd"))
print(a.reverseOnlyLetters(s="a-bC-dEf-ghIj"))
print(a.reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))
