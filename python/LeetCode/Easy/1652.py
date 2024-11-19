# https://leetcode.com/problems/defuse-the-bomb/description/?envType=daily-question&envId=2024-11-18

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        if k == 0:
            return [0] * length
        res = []

        nums = code + code + code

        for i in range(length, 2*length):
            if k > 0:
                res.append(sum(nums[i+1 : i + k + 1]))
            else:
                res.append(sum(nums[i+k : i]))
        return res