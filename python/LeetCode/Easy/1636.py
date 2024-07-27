# https://leetcode.com/problems/sort-array-by-increasing-frequency/?envType=daily-question&envId=2024-07-23

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dictTmp = {}

        for val in nums:
            if val not in dictTmp:
                dictTmp[val] = 0

            dictTmp[val] += 1
        
        cntTmp = {}
        for key in dictTmp:
            val = dictTmp[key]
            if val not in cntTmp:
                cntTmp[val] = []
            
            cntTmp[val].append(key)
        
        res = []
        cntKeyList = sorted(cntTmp.keys())
        for idx in cntKeyList:
            if len(cntTmp[idx]) == 1:
                for _ in range(idx):
                    res.append(cntTmp[idx][0])
            else:
                reverseTmp = sorted(cntTmp[idx], reverse=True)
                for val in reverseTmp:
                    for _ in range(idx):
                        res.append(val)

        return res
        