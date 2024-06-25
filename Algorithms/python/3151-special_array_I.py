class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        i = 0
        while i + 1 < len(nums):
            if nums[i] % 2 == 0 and nums[i + 1] % 2 == 0:
                return False
            elif nums[i] % 2 != 0 and nums[i + 1] % 2 != 0:
                return False
            i += 1
        return True