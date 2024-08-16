class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        
        left = [0]
        right = [0] * len(nums)

        right[len(nums) - 2] = nums[-1]

        for i in range(1, len(nums)):
            left.append(nums[i - 1] + left[i - 1])

        for i in range(len(nums) - 3,  -1, -1):
            right[i] = nums[i + 1] + right[i + 1]
        
        res = []
        for i in range(len(right)):
            res.append(abs(left[i] - right[i]))

        return res

        