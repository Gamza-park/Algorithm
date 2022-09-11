# 17. Letter Combinations of a Phone Number
#
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
          }

        if digits == "":
            return []

        if len(digits) == 1:
            return phone[digits]

        result = phone[digits[0]]

        for i in range(1, len(digits)):
            result = self.sumStringList(result, phone[digits[i]])

        return result

    def sumStringList(self, list1, list2) -> List[str]:
        result = []

        for i in list1:
            for j in list2:
                result.append(i + j)

        return result
