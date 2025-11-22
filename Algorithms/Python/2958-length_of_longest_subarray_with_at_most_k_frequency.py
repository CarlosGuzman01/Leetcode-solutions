class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(nums)):
            dic[nums[r]] += 1
            while dic[nums[r]] > k:
                dic[nums[l]] -= 1
                l += 1
            ans = max(r -l + 1, ans)
        return ans
            



        