# Given a string, find the first non-repeating character in it
#  and return it's index. If it doesn't exist, return -1.

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        countMap = defaultdict(int)
        charArr = [-1] * 256 # Total ASCII chars

        if (s == ""):
            return -1

        for idx in range(len(s)):
            ch = s[idx]
            countMap[ch] += 1
            charArr[ord(ch)] = idx

        for ch, val in countMap.items():
            if (val == 1):
                return charArr[ord(ch)]

        return -1
