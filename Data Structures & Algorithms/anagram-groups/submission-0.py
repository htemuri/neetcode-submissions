from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortMap = defaultdict(list)
        for i, s in enumerate(strs):

            sortMap[''.join(sorted(s))].append(strs[i])
        
        res = []
        for key in sortMap.keys():
            res.append(sortMap[key])
        return res
