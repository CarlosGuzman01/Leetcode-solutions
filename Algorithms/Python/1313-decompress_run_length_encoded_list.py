class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []

        i = 0
        j = 1

        while j < len(nums):
            freq = nums[i]
            val = nums[j]

            for x in range(freq):
                res.append(val)
            i += 2
            j += 2
        return res
        