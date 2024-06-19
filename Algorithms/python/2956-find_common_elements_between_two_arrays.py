class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mySet = set(nums1)
        mySet2 = set(nums2)

        counter = 0
        counter2 = 0

        for n , n2 in zip_longest(nums1, nums2, fillvalue = None):
            if(n in mySet2):
                counter += 1
            if(n2 in mySet):
                counter2 +=1
        

        return [counter, counter2]
            
        