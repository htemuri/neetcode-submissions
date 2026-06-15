from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tupMap = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            tupMap[tuple(counts)].append(s)
        
        return list(tupMap.values())