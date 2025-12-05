class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  
        (-1, -1), (-1, 1), (1, -1), (1, 1)] 

        goal = (len(grid) - 1, len(grid[0]) -1)

        que = deque()
        visited = set()

        visited.add((0,0))
        que.append((0,0))

        steps = 1

        while que:
            for _ in range(len(que)):
                x, y = que.popleft()
                if (x,y) == goal:
                    return steps
                
                for dr, dc in directions:
                    nr = x + dr
                    nc = y + dc

                    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                        continue
                    if (nr, nc) in visited:
                        continue
                    if grid[nr][nc] != 0:
                        continue
                    
                    que.append((nr, nc))
                    visited.add((nr, nc))
            
            steps += 1
        return -1




        