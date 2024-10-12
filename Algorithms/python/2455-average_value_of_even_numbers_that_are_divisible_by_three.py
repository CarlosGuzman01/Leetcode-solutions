class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0

        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                total += n
                count += 1
        
        if count == 0:
            return 0
        return total // count