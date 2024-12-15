class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        myMap = {}
        key = -1
        for n in nums:
            if n % 2 != 0:
                continue 
            if n not in myMap:
                myMap[n] = 1
            else:
                myMap[n] += 1
            
            if key == -1 or myMap[n] > myMap[key] or (myMap[n] == myMap[key] and n < key):
                key = n
        
        if key == -1:
            return -1
        return key
            