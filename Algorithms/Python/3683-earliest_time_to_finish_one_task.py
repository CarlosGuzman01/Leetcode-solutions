class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = float("inf")

        for arr in tasks:
            x, y = arr
            ans = min(ans, x + y)

        return ans
        