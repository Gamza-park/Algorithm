# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        tmp = set()

        for val in nums1:
            set1.add(val)

        for val in nums2:
            if val in set1:
                tmp.add(val)

        return tmp
