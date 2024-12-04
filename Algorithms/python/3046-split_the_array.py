class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        myMap = {}

        for n in nums:
            if n not in myMap:
                myMap[n] = 1
            else:
                myMap[n] += 1
            if myMap[n] > 2:
                return False
                
        return True

        
        