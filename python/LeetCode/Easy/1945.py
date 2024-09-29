# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        asciiList = list(s.encode('ascii'))

        strTmp = ''
        for val in asciiList:
            strTmp += str(val - 96)

        sumTmp = 0
        for _ in range(k):
            sumTmp = 0

            for s in strTmp:
                sumTmp += int(s)
            strTmp = str(sumTmp)

        return sumTmp
        