class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        pos = 0

        for n in nums:
            if n == 0:
                continue
            elif n < 0:
                neg += 1
            else:
                pos += 1
        return max(pos, neg)
        
        