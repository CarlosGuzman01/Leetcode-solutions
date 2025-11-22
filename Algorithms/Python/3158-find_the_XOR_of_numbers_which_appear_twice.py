class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        mySet = set()
        duplicates = []

        for n in nums:
            if n in mySet:
                duplicates.append(n)
            
            mySet.add(n)
        
        if len(duplicates) == 0:
            return 0
        
        total = 0

        for n in duplicates:
            total ^= n

        return total
