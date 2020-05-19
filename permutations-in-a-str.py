class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1), len(s2)
        s1HashSum = sum(map(hash, s1))
        partialS2 = s2[: s1Len]
        s2HashSum = sum(map(hash, partialS2))

        if (s1HashSum == s2HashSum):
            return True

        for i in range(s1Len, s2Len):
            s2HashSum += hash(s2[i]) - hash(s2[i - s1Len])

            if (s2HashSum == s1HashSum):
                return True

        return False
