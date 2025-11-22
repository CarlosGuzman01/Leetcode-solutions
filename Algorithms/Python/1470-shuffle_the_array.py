class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        y = len(nums) // 2
        x = 0
        res = []

        while y < len(nums):
            res.append(nums[x])
            res.append(nums[y])

            x += 1
            y += 1

        return res