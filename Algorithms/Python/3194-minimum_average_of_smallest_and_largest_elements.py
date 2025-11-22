class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        left = 0
        right = len(nums) - 1
        res = sys.maxsize

        while left <= right:
            temp = (nums[left] + nums[right])/2

            res = min(temp, res)

            left += 1
            right -= 1
        return res



            
        