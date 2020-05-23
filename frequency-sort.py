from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        countMap = Counter(s)
        countMap = sorted(countMap.items(), key=lambda x: -x[1])

        res = ''

        for k, v in countMap:
            k *= v

            res += k

        return res
