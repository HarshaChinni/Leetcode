from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_char_dict, s_char_dict = defaultdict(int), defaultdict(int)
        result = []

        if (len(p) > len(s)):
            return result

        for ch in p:
            p_char_dict[ch] += 1

        l, r = 0, 0
        while(r < len(p)):
            s_char_dict[s[r]] += 1
            r += 1

        if (self.isAnagram(s_char_dict, p_char_dict)):
            result.append(0)

        for i in range(len(p), len(s)):
            s_char_dict[s[i-len(p)]] -= 1

            s_char_dict[s[i]] += 1
            if (self.isAnagram(s_char_dict, p_char_dict)):
                result.append(i - len(p) + 1)

        return result

    def isAnagram(self, mainStringDict, anagramDict):
        for k, v in anagramDict.items():
            if not k in mainStringDict:
                return False

            if k in mainStringDict and not v == mainStringDict[k]:
                return False
        return True


class OptimizedSolution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pLen, sLen = len(p), len(s)
        result = []
        
        if (pLen > sLen):
            return result
            
        hashSumP = sum(map(hash, p))
        hashSumS = sum(map(hash, s[:pLen]))
        
        if (hashSumP == hashSumS):
            result.append(0)
        
        for i in range(pLen, sLen):
            hashSumS -= hash(s[i - pLen]) 
            hashSumS += hash(s[i])

            if (hashSumS == hashSumP):
                result.append(i - pLen + 1)

        return result


