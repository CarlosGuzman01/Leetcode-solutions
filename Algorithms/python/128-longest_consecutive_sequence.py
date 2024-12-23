class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0

        s = set()
        ans = 0

        for n in nums:
            s.add(n)
    
        for n in nums:
            if n - 1 not in s:
                length = 1
                while n + length in s:
                    length += 1
                ans = max(ans, length)
        return ans
                
                

        
        