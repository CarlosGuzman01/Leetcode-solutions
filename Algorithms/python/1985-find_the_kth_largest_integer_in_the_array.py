class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        a = ""

        for s in nums:
            heap.append(-int(s))
        
        heapq.heapify(heap)

        for i in range(k):
            a = heapq.heappop(heap)
        
        return str(-a)

        