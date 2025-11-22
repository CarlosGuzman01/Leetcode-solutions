class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        res = []
        map1 = Counter(nums)

        even = 0
        odd = 0

        for key in map1:
            val = map1[key]
            even += val // 2
            odd += val % 2
    
        
        return [even , odd]

        
        