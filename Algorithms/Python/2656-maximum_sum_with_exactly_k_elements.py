class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        can = max(nums)

        res = k * (2 * can + k - 1) // 2
        
        return res