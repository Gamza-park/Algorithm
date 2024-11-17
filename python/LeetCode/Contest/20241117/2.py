# Q2. Zero Array Transformation I

# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

# For each queries[i]:

# - Select a subset of indices within the range [li, ri] in nums.
# - Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.

# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

# A subset of an array is a selection of elements (possibly none) of the array.

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.

class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        length = len(nums)
        diff = [0] * (length + 1)

        for query in queries:
            start, end = query
            diff[start] -= 1
            if end + 1 < length:
                diff[end + 1] += 1

        for i in range(1, length):
            diff[i] += diff[i - 1]

        for i in range(length):
            nums[i] += diff[i]
            if nums[i] < 0:
                nums[i] = 0

        return all(x == 0 for x in nums)
    
        # arrTmp = [0] * (len(nums) * 1)
        # for query in queries:
        #     for idx in range(query[0], query[1]+1):
        #         if nums[idx] == 0 or arrTmp[idx] == nums[idx]:
        #             continue
        #         arrTmp[idx] += 1
        
        # return nums == arrTmp

        #     start, end = query
        #     arrTmp[start] -= 1
        #     if query[1] + 1 < len(nums):
        #         arrTmp[end] += 1
        
        # for idx in range(1, len(arrTmp)):
        #     arrTmp[idx] += arrTmp[idx - 1]
        
        # nums = [nums[idx] + arrTmp[idx] for idx in range(len(nums))]
        
        # print(nums)
        # return all(x == 0 for x in nums)
            
        
        
            
        #     for idx in range(query[0], query[1]+1):
        #         if nums[idx] != 0:
        #             nums[idx] -= 1
        
        # return all(x == 0 for x in nums)
            
        
tmp = Solution()

# [1,0,1]
# [[0,2]]
# [4,3,2,1]
# [[1,3],[0,2]]

# nums = [7]
# queries = [[0,0]]

nums = [1,0,1]
queries = [[0,2]]

tmp.isZeroArray(nums, queries)