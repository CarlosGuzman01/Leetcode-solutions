class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        temp = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                temp += nums[i]
            else:
                temp = nums[i]
            ans = max(temp, ans)
        return ans

