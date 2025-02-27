# 내풀이
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        s_count = len(s)
        for left in range(len(t)):
            right = left + 1
            if t[left] == s[0]:
                s_count -= 1
                while left < right < len(t):
                    if s[-s_count] == t[right]:
                        s_count -= 1
                        if s_count == 0:
                            return True
                    right += 1
                if s_count == 0:
                    return True
                else:
                    return False
        return False


# 성능이제일좋은 답변풀이
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        a, b = 0, 0
        while a < len(s) and b < len(t):
            if s[a] == t[b]:
                a += 1
            b += 1
        return a == len(s)


a = Solution()
print(a.isSubsequence(s="aaaaaa", t="bbaaaa"))
print(
    a.isSubsequence(
        s="rjufvjafbxnbgriwgokdgqdqewn",
        t="mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq",
    )
)
print(a.isSubsequence(s="b", t="abc"))
print(a.isSubsequence(s="abc", t=""))
print(a.isSubsequence(s="", t="ahbgdc"))
print(a.isSubsequence(s="abc", t="ahbgdc"))
print(a.isSubsequence(s="axc", t="ahbgdc"))
