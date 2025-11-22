class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        res = []

        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                res.append(n)
            nums[n - 1] = -nums[n -  1]
        

        for i in range(len(nums)):
            if nums[i] > 0 and i + 1 != res[0]:
                res.append(i + 1)
        
        return res