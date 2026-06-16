from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1

        maj = len(nums) // 2
        for key in countMap.keys():
            if countMap[key] > maj:
                return key
        return
