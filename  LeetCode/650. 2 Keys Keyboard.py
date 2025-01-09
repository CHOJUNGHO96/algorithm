"""
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.



Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0


Constraints:

1 <= n <= 1000

화면에 문자 'A'가 하나만 있는 메모장이 있습니다. 이 메모장에서 매 단계마다 아래 두 가지 작업 중 하나를 수행할 수 있습니다:

모두 복사 (Copy All): 화면에 있는 모든 문자를 복사합니다. (일부만 복사는 불가능합니다.)
붙여넣기 (Paste): 마지막에 복사된 문자를 화면에 붙여넣습니다.
정수 n이 주어졌을 때, 화면에 문자 'A'를 정확히 n개 만들기 위해 필요한 최소 작업 수를 반환하세요.

예제 1:
입력: n = 3
출력: 3
설명:

처음에는 화면에 'A'가 1개 있습니다.
1단계: 모두 복사(Copy All) 작업을 수행합니다.
2단계: 붙여넣기(Paste) 작업으로 'AA'를 만듭니다.
3단계: 다시 붙여넣기(Paste) 작업으로 'AAA'를 만듭니다.
총 작업 수는 3입니다.
예제 2:
입력: n = 1
출력: 0
설명: 이미 화면에 'A'가 1개 있으므로 작업이 필요하지 않습니다.

제약 사항:
1 <= n <= 1000
"""
import math


class Solution:
    @classmethod
    def minSteps(cls, 기준값):
        작업_수 = 0
        소인수 = 2
        while 기준값 > 1:
            while 기준값 % 소인수 == 0:
                작업_수 += 소인수
                기준값 //= 소인수
            소인수 += 1
        return 작업_수


print(Solution.minSteps(18))
print(Solution.minSteps(6))
print(Solution.minSteps(7))
print(Solution.minSteps(4))
print(Solution.minSteps(1))
print(Solution.minSteps(3))
