class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        myMap = Counter(tasks)
        que = deque()
        heap = []

        for c in myMap:
            heap.append([-myMap[c], c])

        heapq.heapify(heap) 
        i = 0
        
        while que or heap:
            if len(heap) > 0:
                count , c = heapq.heappop(heap)
                count = -count -1

                if count > 0:
                    que.append([count, c , i + n])

            if que and que[0][2] == i:
                count, c, time = que.popleft()
                heapq.heappush(heap, [-count, c])
                  
            i+=1
        return i