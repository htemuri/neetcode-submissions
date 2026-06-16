class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for num in nums:
            if num == val:
                count += 1
        
        k = len(nums) - count

        while val in nums[:k]:
            for i in range(k):
                if nums[i] == val:
                    # shift to end
                    temp = nums[i]
                    for j in range(i+1, len(nums)):
                        nums[j-1] = nums[j]
                    nums[-1] = temp
                
        return k