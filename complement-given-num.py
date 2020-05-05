# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        binNum = bin(num)
        complementStr = ''

        binNum = binNum.replace('0b', '')

        for i in binNum:
            if (i == '1'):
                complementStr += '0'

            if (i == '0'):
                complementStr += '1'

        return int(complementStr, 2)
