class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        heap = []
        map1 = Counter(arr)
        total = 0
        ans = 0

        for key in map1:
            heap.append(-map1[key])
        
        heapq.heapify(heap)

        while total * 2 < len(arr):
            val = -heapq.heappop(heap)
            total += val
            ans += 1 
        return ans
        