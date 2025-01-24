class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        i = 0
        j = 1

        for n in nums:
            if n > 0:
                res[i] = n
                i += 2
            else:
                res[j] = n
                j += 2
        return res


        