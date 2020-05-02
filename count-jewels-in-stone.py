class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewelSet = set()
        jewelStoneCount = 0

        for j in J:
            jewelSet.add(j)

        for s in S:
            if s in jewelSet:
                jewelStoneCount += 1

        return jewelStoneCount
