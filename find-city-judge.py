from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustMap = defaultdict(set)
        res = []

        for person in trust:
            trustMap[person[0]].add(person[1])

        for label in range(1, N + 1):
            if label not in trustMap:
                res.append(label)

        if (len(res) == 1):
            label = res.pop()
            for trustees in trustMap.values():
                if (not label in trustees):
                    return -1

            return label
        else:
            return -1
