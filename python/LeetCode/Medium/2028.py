# https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        result = []

        lenTotal = len(rolls) + n
        diff = (lenTotal * mean) - sum(rolls)

        if 6 * n < diff or n > diff:
            return result

        if diff % n == 0:
            for _ in range(n):
                result.append(diff // n)
        else:
            rest = diff % n
            for _ in range(n):
                result.append(diff // n)
            
            while rest != 0:
                for idx in range(n):
                    result[idx] += 1
                    rest -= 1

                    if rest == 0:
                        break

        return result
