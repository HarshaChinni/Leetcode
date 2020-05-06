from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        majorityNum = None

        for num in nums:
            countMap[num] += 1

            if (countMap[num] > len(nums)//2):
                majorityNum = num

        return majorityNum
