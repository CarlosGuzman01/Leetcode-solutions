class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        icount = 1
        dcount = 1
        res = 1
        i = 0

        while i + 1 < len(nums):

            if nums[i] < nums[i + 1]:
                icount += 1
                res = max(icount, res)
            else:
                icount = 1
            
            if nums[i] > nums[i + 1]:
                dcount += 1
                res = max(dcount, res)
            else:
                dcount = 1

            i += 1

        
        return res

        