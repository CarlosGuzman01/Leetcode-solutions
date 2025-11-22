class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            if n % 2 == 0: total |= n
        return total

        