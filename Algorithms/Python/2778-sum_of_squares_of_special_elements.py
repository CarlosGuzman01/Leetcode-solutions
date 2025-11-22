class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        size = len(nums)

        for i, n in enumerate(nums):
            if size % (i + 1) == 0:
                
                res += n * n
        return res