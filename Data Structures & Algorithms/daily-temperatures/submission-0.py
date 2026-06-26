class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force

        res = []
        for i in range(len(temperatures)):
            found = False
            for j in range(i+1, len(temperatures)):
                if found:
                    continue
                if temperatures[i] < temperatures[j]:
                    res.append(j-i)
                    found = True
            if found == False:
                res.append(0)
        return res