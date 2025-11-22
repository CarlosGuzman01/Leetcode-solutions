class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []

        map1 = Counter(words)

        for key in map1:
            heap.append((-map1[key], key))
        
        heapq.heapify(heap)
        
        res = []
        
        for i in range(k):
            _, value = heapq.heappop(heap)
            res.append(value)

        return res
        