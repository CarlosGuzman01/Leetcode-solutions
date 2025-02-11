class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        s = set()
        heap = []

        for i in range(len(nums)):
            heap.append([nums[i], i])
        
        heapq.heapify(heap)

        while heap:
            val, ind = heapq.heappop(heap)

            if ind not in s:
                if ind + 1 <= len(nums):
                    s.add(ind + 1)
                if ind - 1 >= 0:
                    s.add(ind - 1)
                score += val
        return score
            








        