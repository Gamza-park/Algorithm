# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/?envType=daily-question&envId=2024-09-01

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        result = []
        tmp = []
        for val in original:
            tmp.append(val)

            if len(tmp) == n:
                result.append(tmp)
                tmp = []

        return result
