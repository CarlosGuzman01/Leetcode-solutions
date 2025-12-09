class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)

        for edge in edges:
            x, y = edge
            graph[x].append(y)
            graph[y].append(x)
        

        visited = set()
        def dfs(n):
            if n == destination:
                return True
            
            visited.add(n)
            for x in graph[n]:
                if x not in visited:
                    if dfs(x): return True
            return False
        
        return dfs(source)