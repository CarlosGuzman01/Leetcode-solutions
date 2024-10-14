class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        count = 0
        heap = [-x for x in nums]

        heapq.heapify(heap)

        while k:
            
            value = -heapq.heappop(heap)
            count += value
            heapq.heappush(heap, -ceil(value/3))

            k -= 1
        
        return count