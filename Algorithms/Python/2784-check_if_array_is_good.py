class Solution:
    def isGood(self, nums: List[int]) -> bool:

        myMap = {}

        highest = -1

        for n in nums:
            if n not in myMap:
                myMap[n] = 1
            else:
                myMap[n] += 1
            if myMap[n] > 2 or (n != len(nums) - 1 and myMap[n] > 1):
                return False

            highest = max(highest, n)

        if len(nums) != highest + 1:
            return False

        return True
