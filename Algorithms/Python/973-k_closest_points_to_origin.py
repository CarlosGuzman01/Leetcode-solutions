class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        
        for x, y in points:
            dis = (x ** 2) + (y ** 2)
            heapq.heappush(heap, [dis, x, y])
        
        result = []
        for i in range(k):
           dist, x, y = heapq.heappop(heap)
           result.append([x, y])
        
        return result

        
