# https://leetcode.com/problems/find-if-array-can-be-sorted/description/?envType=daily-question&envId=2024-11-06

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevMax, currMin, currMax = 0, 0, 0
        prevBit = -1
        for num in nums:
            bCnt = num.bit_count()
            if prevBit != bCnt:
                if currMin<prevMax: return False
                prevMax = currMax
                currMin, currMax=num, num
                prevBit = bCnt
            else:
                currMin = min(currMin, num)
                currMax = max(currMax, num)
        return currMin >= prevMax
