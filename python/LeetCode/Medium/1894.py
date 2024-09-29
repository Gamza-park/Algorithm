# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/?envType=daily-question&envId=2024-09-02

class Solution:
    # def chalkReplacer(self, chalk: List[int], k: int) -> int:
    #     idx = 0
    #     idxMax = len(chalk) - 1
    #     while True:
    #         k -= chalk[idx]
    #         if k < 0:
    #             break
    #         idx += 1

    #         if idx > idxMax:
    #             idx = 0
        
    #     return idx

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        idxMax = len(chalk) - 1
        chalkSum = sum(chalk)

        rest = k % chalkSum

        for idx in range(len(chalk)):
            rest -= chalk[idx]
            if rest < 0:
                return idx
