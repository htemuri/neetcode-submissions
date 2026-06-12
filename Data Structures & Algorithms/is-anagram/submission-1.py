class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = collections.defaultdict(int)
        t_counts = collections.defaultdict(int)

        for char in s:
            s_counts[char] += 1
        
        for char in t:
            t_counts[char] += 1
    
        return s_counts == t_counts