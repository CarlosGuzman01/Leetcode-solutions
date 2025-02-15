class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        map1 = {}

        for i in range(len(nums)):
            map1[nums[i]] = i

        for arr in operations:
            find, replace = arr

            i = map1[find]
            nums[i] = replace

            del map1[find]
            map1[replace] = i
        
        return nums












        