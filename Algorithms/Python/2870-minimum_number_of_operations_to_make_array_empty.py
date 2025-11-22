class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        map1 = Counter(nums)
        res = 0

        for i in map1:

            if map1[i] == 1:
                return -1

            res += math.ceil(map1[i]/3)
        return res
            


            