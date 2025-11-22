class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            v = abs(n) - 1
            nums[v] = -abs(nums[v])
        

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res



        