from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charMap = defaultdict(int)

        for m in magazine:
            charMap[m] += 1

        for r in ransomNote:
            if not charMap[r]:
                return False

            charMap[r] -= 1

        return True
