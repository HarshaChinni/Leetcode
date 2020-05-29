class Solution:
    def countBits(self, num: int) -> List[int]:
        if (num <= 1):
            return [0, 1] if num else [0]
        else:
            bitCntArr = [0] * (num + 1)
            bitCntArr[0], bitCntArr[1] = 0, 1

            for n in range(2, num + 1):
                quotient = n // 2
                remainder = n % 2
                bitCntArr[n] += bitCntArr[quotient] + bitCntArr[remainder]

        return bitCntArr
