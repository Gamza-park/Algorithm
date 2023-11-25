# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        liTmp = []
        tmp = []

        for val in nums1:
            liTmp.append(val)

        for val in nums2:
            if val in liTmp:
                liTmp.remove(val)
                tmp.append(val)

        return tmp
