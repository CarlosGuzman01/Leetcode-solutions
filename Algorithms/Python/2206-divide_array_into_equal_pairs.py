class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        map = Counter(nums)

        for key in map:
            if map[key] % 2 != 0:
                return False
        return True