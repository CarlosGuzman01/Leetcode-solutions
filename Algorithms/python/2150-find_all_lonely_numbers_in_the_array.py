class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        ans = []

        myMap = Counter(nums)

        for n in nums:
            if myMap[n] == 1 and n + 1 not in myMap and n - 1 not in myMap:
                ans.append(n)
        return ans

                



                    
                    


        