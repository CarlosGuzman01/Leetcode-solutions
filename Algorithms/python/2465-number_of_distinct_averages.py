class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
    
        nums.sort()

        left = 0
        right = len(nums) - 1
        mySet = set()

        while left < right:
            mySet.add((nums[left] + nums[right])/2)

            left += 1
            right -= 1
        return len(mySet)


