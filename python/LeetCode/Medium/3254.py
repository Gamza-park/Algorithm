# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/?envType=daily-question&envId=2024-11-16

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        result = []
        for idx in range(len(nums) - (k - 1)):
            arrTmp = nums[idx: idx+k]
            if self.checkSortedArray(arrTmp):
                if self.checkIncreasesOne(arrTmp, k):
                    result.append(arrTmp[len(arrTmp)-1])
                    continue

            result.append(-1)

        return result

    def checkSortedArray(self, arr: List[int]) -> bool:
        if arr[len(arr)-1] == arr[0]:
            return False

        return arr == sorted(arr)

    def checkIncreasesOne(self, arr: List[int], k) -> bool:
        checkSet = set(arr)
        if arr[0] + (k - 1) == arr[len(arr)-1] and len(checkSet) == k:
            return True

        return False
