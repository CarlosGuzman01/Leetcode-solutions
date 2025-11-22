class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        j = 1
        i = 0
        while j < len(nums):
            total += min(nums[i], nums[j])
            i+=2
            j+=2
        return total
        