class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(list(s))
        t_sorted = sorted(list(t))
        return s_sorted == t_sorted