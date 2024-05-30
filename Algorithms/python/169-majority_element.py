class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        count = 0

        for i in nums:
            if result == i:
                count += 1
            elif count == 0:
                result = i
            else:
                count -= 1

        return result
