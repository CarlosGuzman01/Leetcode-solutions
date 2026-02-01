class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        arr = sorted(nums[1:])
        return arr[0] + arr[1] + nums[0]
        