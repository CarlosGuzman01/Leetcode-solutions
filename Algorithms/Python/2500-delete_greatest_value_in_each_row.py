class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        p = len(grid[0]) - 1
        ans = 0
        for i in range(len(grid[0])):
            val = []
            for arr in grid:
                arr.sort()
                val.append(arr[p])
            p -= 1
            ans += max(val)
        return ans

        