class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        r1 = set()
        r2 = set()

        for n in nums1:
            if n not in s2:
                r1.add(n)
        
        for n in nums2:
            if n not in s1:
                r2.add(n)
        

        return [list(r1), list(r2)]


        