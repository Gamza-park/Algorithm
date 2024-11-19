# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/?envType=daily-question&envId=2024-11-19

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxValue = 0
        arrSum = 0
        check = set()

        tmp = {}

        for idx in range(len(nums)):
            arrSum += nums[idx]
            check.add(nums[idx])

            if nums[idx] not in tmp:
                tmp[nums[idx]] = 1
            else:
                tmp[nums[idx]] += 1

            if idx >= k:
                arrSum -= nums[idx - k]

                tmp[nums[idx - k]] -= 1
                if tmp[nums[idx - k]] == 0:
                    check.discard(nums[idx - k])

            if len(check) == k and maxValue < arrSum:
                maxValue = arrSum

        return maxValue



        # maxValue = 0
        
        # for idx in range(len(nums) - k + 1):
        #     setTmp = set(nums[idx : idx + k])
        #     if len(setTmp) == k:
        #         arrSum = sum(nums[idx : idx + k])
        #         if maxValue < arrSum:
        #             maxValue = arrSum

        # return maxValue
                 

        