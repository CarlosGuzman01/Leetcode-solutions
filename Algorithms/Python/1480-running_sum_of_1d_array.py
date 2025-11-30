class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        total = 0
        for i in range(len(nums)):
            arr.append(total + nums[i])
            total += nums[i]
        return arr

        