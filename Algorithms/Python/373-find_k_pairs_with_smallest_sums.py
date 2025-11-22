class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []

        for i in range(len(nums1)):
            heap.append((nums1[i] + nums2[0], i, 0))

        heapq.heapify(heap)
        
        ans = []

        while k > 0 and heap:
            _, i1, i2 = heapq.heappop(heap)
            ans.append([nums1[i1], nums2[i2]])

            if i2 + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
            
            k -= 1
        return ans
        