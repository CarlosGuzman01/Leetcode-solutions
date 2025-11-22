class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return -1

        maxVal = 0
        minVal = 101

        for n in nums:
            maxVal = max(n, maxVal)
            minVal = min(n, minVal)
        
        for n in nums:
            if n != minVal and n != maxVal:
                return n


        return -1


        