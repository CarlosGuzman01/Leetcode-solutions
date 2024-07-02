class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        map = Counter(nums1)
        res = []
        for n in nums2:
            if n in map and map[n] > 0:
                res.append(n)
                map[n] += -1
        return res

