class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        winner = [0,0]

        for i in range(len(grid)):
            total = 0
            for n in grid[i]:
                if n == 1:
                    total += 1
            if total > winner[1]:
                winner[0] = i
                winner[1] = total
        return winner[0]


                



        