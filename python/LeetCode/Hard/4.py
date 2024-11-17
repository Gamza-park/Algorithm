# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sumArr = sorted(nums1 + nums2)
        if len(sumArr) % 2 == 1:
            return sumArr[len(sumArr) // 2]
        
        midIdx = len(sumArr) // 2

        return (sumArr[midIdx] + sumArr[midIdx - 1]) / 2
        