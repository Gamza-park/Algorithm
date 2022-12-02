# 190. Reverse Bits
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
# Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
#
# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        strTmp = str(bin(n))[2:]
        if len(strTmp) != 32:
            strTmp = "0" * (32 - len(strTmp)) + strTmp
        bit = 1
        res = 0
        for val in strTmp:
            res += bit * int(val)
            if bit == 1:
                bit = 2
            else:
                bit *= 2

        return res
