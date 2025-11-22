class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = nums[0]

        for n in nums:
            total = 0
            while n > 0:
                digit = n % 10
                total += digit
                n = n // 10
            res = min(res, total)
        return res

        