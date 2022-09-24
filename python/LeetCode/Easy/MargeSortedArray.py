# 88. Merge Sorted Array
#
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.delete(nums1, m)
        self.insert(nums1, nums2, n)
        nums1.sort()

    def delete(self, nums: List[int], n: int):
        for i in reversed(range(n, len(nums))):
            nums.remove(nums[i])

    def insert(self, nums1: List[int], nums2: List[int], n: int):
        # nums1 += nums2
        for i in range(n):
            nums1.append(nums2[i])
