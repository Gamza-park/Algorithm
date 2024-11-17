# Q1. Make Array Elements Equal to Zero

# You are given an integer array nums.

# Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.

# After that, you repeat the following process:

# If curr is out of the range [0, n - 1], this process ends.
# If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
# Else if nums[curr] > 0:
# Decrement nums[curr] by 1.
# Reverse your movement direction (left becomes right and vice versa).
# Take a step in your new direction.
# A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.

# Return the number of possible valid selections.

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.

class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        cnt = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                continue
            print(nums[curr], curr, nums)
            if self.checkSolution(nums, True, curr):
                cnt += 1
            if self.checkSolution(nums, False, curr):
                cnt += 1
                
        return cnt
            
    def checkSolution(self, inputArr, flag, startIdx):
        idxTmp = startIdx
        arr = inputArr[:]
        
        print(flag)
        
        while True:
            if arr[idxTmp] != 0:
                arr[idxTmp] = arr[idxTmp] - 1
                flag = not flag
    
            if arr[idxTmp] < 0:
                break
    
            if flag:
                idxTmp += 1
            else:
                idxTmp -= 1
    
            if idxTmp < 0 or idxTmp > len(arr) - 1:
                break
        print(arr, startIdx)
        return len(set(arr)) == 1
    
tmp = Solution()

print(tmp.countValidSelections(nums=[1,0,2,0,3]))