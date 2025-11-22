class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        highest = -999
        lowest = 999
        
        for n in divisors:
            count = 0
            for x in nums:
                if x % n == 0:
                    count += 1
            if(highest < count or (highest == count and lowest > n)):
                highest = count
                lowest = n
        return lowest
