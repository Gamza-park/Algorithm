# g

class Solution:
    def mySqrt(self, x: int) -> int:
        tmp = 0.0
        res = x/2
        while res != tmp:
            tmp = res
            res = ((x/tmp)+tmp)/2
        return int(res)