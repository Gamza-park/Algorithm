# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            # 빈배열 예외처리
            return ""
        elif len(strs) == 1:
            # 배열 값이 1개일경우 예외처리
            return strs[0]
        else:
            min = self.getMinlen(strs)
            minLength = 3000
            for i in range(len(strs) - 1):
                # i 인덱스는 단어의 갯수
                cnt = 0
                for j in range(min):
                    # j 인덱스는 문자열 수
                    # min값을 구해 최소한만 반복문이 돌도록 설계
                    if strs[i][j] == strs[i + 1][j]:
                        # 글자가 같을 경우 카운트
                        cnt += 1
                    else:
                        # 문자가 다를 경우 j반복문 종료
                        break
                # minLength값 구하기.
                if minLength > cnt:
                    minLength = cnt

            if minLength == 0:
                return ""
            else:
                return strs[0][0:minLength]

    def getMinlen(self, strs: List[str]) -> int:
        min = 4000
        for i in range(len(strs)):
            if min > len(strs[i]):
                min = len(strs[i])
        return min