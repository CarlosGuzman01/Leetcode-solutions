class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]

        heapq.heapify(gifts)

        for i in range(k):
            heapq.heappush(gifts, -floor(sqrt(-heapq.heappop(gifts))))

        total = 0

        for n in gifts:
            total += abs(n)
        return int(total)
