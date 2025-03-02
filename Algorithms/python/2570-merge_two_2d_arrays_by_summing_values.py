class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        res = []

        while p1 < len(nums1) and p2 < len(nums2):
            v1 = nums1[p1][0]
            v2 = nums2[p2][0]

            s1 = nums1[p1][1]
            s2 = nums2[p2][1]

            if v1 == v2:
                res.append([v1,s1 + s2])
                p1 += 1
                p2 += 1
                
            else:
                if v1 < v2:
                    res.append([v1, s1])
                    p1 += 1
                   
                else:
                    res.append([v2, s2])
                    p2 += 1
        
        while p1 < len(nums1):
            v1 = nums1[p1][0]
            v2 = nums1[p1][1]

            res.append([v1, v2])

            p1 += 1
        
        while p2 < len(nums2):
            v1 = nums2[p2][0]
            v2 = nums2[p2][1]

            res.append([v1, v2])

            p2 += 1

        return res









        
        