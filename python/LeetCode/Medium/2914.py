# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/?envType=daily-question&envId=2024-11-05

class Solution:
    def minChanges(self, s: str) -> int:
        cnt = 0

        for idx in range(0, len(s), 2):
            if s[idx] != s[idx+1]:
                cnt += 1
        return cnt

        