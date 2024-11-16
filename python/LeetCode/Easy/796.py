# https://leetcode.com/problems/rotate-string/description/?envType=daily-question&envId=2024-11-03

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        return goal in s+s