class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        res = []
        heap = []

        for arr in score:
            heap.append([-arr[k], arr])

        heapq.heapify(heap)

        while heap:
            x, arr = heapq.heappop(heap)

            res.append(arr)

        return res


        
        