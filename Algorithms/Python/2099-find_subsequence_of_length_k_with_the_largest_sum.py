class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for n in nums:
            heap.append(-n)

        heapq.heapify(heap)

        dict1 = defaultdict(int)
        p = k
        while k:
            dict1[-heapq.heappop(heap)]+= 1 
            k -= 1
            
        res = []

        for n in nums:
            if n in dict1 and dict1[n] > 0:
                res.append(n)
                dict1[n] -= 1
            if len(res) == p:
                break
        return res