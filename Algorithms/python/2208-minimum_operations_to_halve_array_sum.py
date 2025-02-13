class Solution:
    def halveArray(self, nums: List[int]) -> int:

        counter = 0
        heap = []
        total = 0

        for n in nums:
            heap.append(-n)
            total += n
        
        heapq.heapify(heap)
        
        temp  = 0
        while temp < total /2:            
            v = heapq.heappop(heap)
            v = -v
            heapq.heappush(heap, -v/2)
            temp += (v/2)
            counter += 1

        return counter
        