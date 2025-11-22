class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        small = 1001
        big = -1

        for n in nums:
            small = min(n, small)
            big = max(n, big)
        
        return gcd(small, big)
        