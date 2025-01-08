"""
0-인덱스 배열인 words (문자열 배열)과 2D 정수 배열 queries가 주어집니다.

각 쿼리는 queries[i] = [li, ri] 형태이며, 배열 words의 인덱스 범위 [li, ri](포함)에서 모음으로 시작하고 모음으로 끝나는 문자열의 개수를 찾으라는 요청입니다.

queries.length와 같은 크기의 배열 ans를 반환하세요. 여기서 ans[i]는 i번째 쿼리에 대한 답입니다.

참고로, 모음은 'a', 'e', 'i', 'o', 'u'입니다.
"""
from typing import List


class Solution:
    @classmethod
    def vowelStrings1(cls, 단어들: List[str], 쿼리들: List[List[int]]) -> List[int]:
        모음모음 = set("aeiou")
        첫자끝자_리스트 = [1 if 단어[0] in 모음모음 and 단어[-1] in 모음모음 else 0 for 단어 in 단어들]
        정답 = []

        for 쿼리 in 쿼리들:
            합계값 = sum(첫자끝자_리스트[쿼리[0] : 쿼리[-1] + 1])
            정답.append(합계값)
        return 정답

    @classmethod
    def vowelStrings(cls, 단어들: List[str], 쿼리들: List[List[int]]) -> List[int]:
        모음 = set("aeiou")

        모음시작끝 = [1 if 단어[0] in 모음 and 단어[-1] in 모음 else 0 for 단어 in 단어들]

        누적합 = [0] * (len(단어들) + 1)
        for i in range(len(단어들)):
            누적합[i + 1] = 누적합[i] + 모음시작끝[i]

        결과 = []
        # 시작과 끝 사이에 모음의 개수만 알면됨
        for 쿼리 in 쿼리들:
            시작, 끝 = 쿼리
            결과.append(누적합[끝 + 1] - 누적합[시작])

        return 결과


print(Solution.vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1], [4, 4]]))
print(Solution.vowelStrings(["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]))
print(
    Solution.vowelStrings(
        [
            "bzmxvzjxfddcuznspdcbwiojiqf",
            "mwguoaskvramwgiweogzulcinycosovozppl",
            "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs",
            "uivcdsboxnraqpokjzaayedf",
            "yalc",
            "bbhlbmpskgxmxosft",
            "vigplemkoni",
            "krdrlctodtmprpxwditvcps",
            "gqjwokkskrb",
            "bslxxpabivbvzkozzvdaykaatzrpe",
            "qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi",
            "siqbezhkohmgbenbkikcxmvz",
            "ddmaireeouzcvffkcohxus",
            "kjzguljbwsxlrd",
            "gqzuqcljvcpmoqlnrxvzqwoyas",
            "vadguvpsubcwbfbaviedr",
            "nxnorutztxfnpvmukpwuraen",
            "imgvujjeygsiymdxp",
            "rdzkpk",
            "cuap",
            "qcojjumwp",
            "pyqzshwykhtyzdwzakjejqyxbganow",
            "cvxuskhcloxykcu",
            "ul",
            "axzscbjajazvbxffrydajapweci",
        ],
        [
            [4, 4],
            [6, 17],
            [10, 17],
            [9, 18],
            [17, 22],
            [5, 23],
            [2, 5],
            [17, 21],
            [5, 17],
            [4, 8],
            [7, 17],
            [16, 19],
            [7, 12],
            [9, 20],
            [13, 23],
            [1, 5],
            [19, 19],
        ],
    )
)
