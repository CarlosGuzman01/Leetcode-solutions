class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s =  set(nums)
        v = original
        while v in s:
            v *= 2
        return v
