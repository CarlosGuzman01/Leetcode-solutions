class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        mySet = set(nums[0])

        for i in range(1, len(nums)):
            mySet &= set(nums[i])
        return sorted(mySet)

