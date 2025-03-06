class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {0:1, 1:1}

        def dp(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = dp(x - 1) + dp(x - 2)
                return memo[x]
        return dp(n)