# https://leetcode.com/problems/string-compression-iii/description/?envType=daily-question&envId=2024-11-04

class Solution:
    def compressedString(self, word: str) -> str:
        length = 0
        checkWord = ''
        res = ''

        for char in word:
            if checkWord == '':
                checkWord = char
            elif char != checkWord or length == 9:
                res += str(length) + checkWord
                checkWord = char
                length = 0
            
            length += 1

        res += str(length) + word[-1]

        return res