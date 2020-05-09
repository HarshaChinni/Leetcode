from sys import setrecursionlimit

setrecursionlimit(10**6)


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num == 1):
            return True

        return self.isPerfectSquareHelper(1, num, num)

    def isPerfectSquareHelper(self, start, end, actualNum):
        mid = start + (end - start)//2

        if (mid * mid == actualNum):
            return True

        if (mid == 1 or mid == 0):
            return False
        elif (mid * mid < actualNum < (mid + 1) * (mid + 1)):
            return False

        if (mid * mid > actualNum):
            return self.isPerfectSquareHelper(start, mid - 1, actualNum)
        else:
            return self.isPerfectSquareHelper(mid + 1, end, actualNum)
