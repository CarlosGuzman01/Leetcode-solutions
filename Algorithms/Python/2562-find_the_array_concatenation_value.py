class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        total = 0

        low = 0
        high = len(nums) - 1

        while low < high:

            total += int(str(nums[low]) + str(nums[high]))

            low += 1
            high -= 1


        if len(nums) % 2 != 0:
            total += nums[low]
        return total 

        