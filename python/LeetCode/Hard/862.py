# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/?envType=daily-question&envId=2024-11-17

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        length = len(nums)
        prefixSum = [0] * (length + 1)
        
        for i in range(1, length + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
            
        minLength = inf
        
        deque = []
        
        for i in range(length + 1):
            while deque and prefixSum[i] - prefixSum[deque[0]] >= k:
                minLength = min(minLength, i - deque.pop(0))
                
            while deque and prefixSum[i] <= prefixSum[deque[-1]]:
                deque.pop()
                
            deque.append(i)
        
        if minLength == inf:
            return -1
        
        return minLength 
        
        # minLength = inf
        # for i in range(len(nums)):
        #     sumTmp = 0
        #     for j in range(i, len(nums)):
        #         sumTmp += nums[j]

        #         if sumTmp >= k:
        #             if (j+1) - i < minLength:
        #                 minLength = (j+1) - i
        #             break
                    
        # if minLength == inf:
        #     return -1

        # return minLength
    
tmp = Solution()

tmp.shortestSubarray([2, -1, 2], 3)
        

