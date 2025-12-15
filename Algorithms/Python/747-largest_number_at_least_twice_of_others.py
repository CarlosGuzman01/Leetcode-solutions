class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = float("-inf")
        second_largest = float("-inf")
        largest_i = 0

        for i, n in enumerate(nums):
            if n > largest:
                second_largest = largest
                largest = n
                largest_i = i
            elif n > second_largest:
                second_largest = n
        
        if second_largest * 2 > largest:
            return -1
        return largest_i


        