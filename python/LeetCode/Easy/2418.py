# https://leetcode.com/problems/sort-the-people/?envType=daily-question&envId=2024-07-22

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tmpDict = {}
        for idx in range(len(names)):
            tmpDict[heights[idx]] = names[idx]
        

        sortHeightArr = sorted(heights, reverse=True)
        res = []
        for height in sortHeightArr:
            res.append(tmpDict[height])

        return res
            
        