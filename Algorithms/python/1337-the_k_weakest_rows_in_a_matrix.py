class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for i in range(len(mat)):
            count = 0
            for n in mat[i]:
                if n == 1: count += 1
            heap.append([count, i])
        
        heapq.heapify(heap)
        res = []
        while k:
            count , v = heapq.heappop(heap)
            res.append(v)
            k -= 1
        return res


        