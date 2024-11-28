class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if n == 0:
            return 
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        s = len(nums1) - 1
        m = m - 1
        n = n - 1

        while m >= 0 and n >=0:
            if nums1[m] > nums2[n]:
                nums1[s] = nums1[m]
                s -= 1
                m -= 1
            else:
                nums1[s] = nums2[n]
                s -= 1
                n -= 1
        
        if(m >= 0):
            for i in range(m + 1):
                nums1[i] = nums1[i]
        if(n >= 0):
            for i in range(n + 1):
                nums1[i] = nums2[i]
        return 

            
            




        

        


        
        
        