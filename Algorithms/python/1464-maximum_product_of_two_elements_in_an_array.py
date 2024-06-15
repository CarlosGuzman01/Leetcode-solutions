class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-x for x in nums]

        heapq.heapify(nums)

        val1 = -heapq.heappop(nums)
        val2 = -heapq.heappop(nums)

        return (val1 - 1) * (val2 - 1)
        