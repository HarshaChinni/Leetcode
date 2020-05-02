# Question START

# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Question ENDS


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.__firstBadVersionHelper(n)
        # return self.__firstBadVersionRecursionHelper(1, n)

    def __firstBadVersionHelper(self, version):
        start = 1
        end = version

        while (start <= end):
            mid = start + (end - start)//2
            isMidVersionBad = isBadVersion(mid)

            if (isMidVersionBad and not isBadVersion(mid - 1)):
                return mid

            if (isMidVersionBad):
                end = mid - 1
            else:
                start = mid + 1

    def __firstBadVersionRecursionHelper(self, start, end):
        mid = start + (end - start)//2
        isMidVersionBad = isBadVersion(mid)

        if (isMidVersionBad and not isBadVersion(mid-1)):
            return mid

        if (isMidVersionBad):
            return self.__firstBadVersionHelper(start, mid - 1)
        else:
            return self.__firstBadVersionHelper(mid + 1, end)
