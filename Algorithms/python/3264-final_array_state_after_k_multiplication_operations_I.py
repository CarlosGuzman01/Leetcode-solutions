class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        for i in range(len(nums)):
            heap.append([nums[i], i])

        heapq.heapify(heap)

        for i in range(k):
            val, index = heapq.heappop(heap)
            val *= multiplier
            nums[index] = val
            heapq.heappush(heap, [val, index])

        return nums
