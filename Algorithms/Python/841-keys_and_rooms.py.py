class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        visited.add(0)

        que = deque([0])

        while que:
            room = que.popleft()
            for key in rooms[room]:
                if key not in visited:
                    que.append(key)
            visited.add(room)
        

        return len(rooms) == len(visited)
        



        