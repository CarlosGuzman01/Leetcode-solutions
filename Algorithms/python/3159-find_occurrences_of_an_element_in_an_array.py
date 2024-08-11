class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        index = []

        for i in range(len(nums)):
            if nums[i] == x:
                index.append(i)

        res = []
        for n in queries:
            if len(index) <= n - 1:
                res.append(-1)
            else:
                res.append(index[n - 1])
        return res
