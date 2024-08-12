class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0

        for n in nums:
            if n <= 9:
                single += n
            else:
                double += n
        
        if single == double:
            return False
        return True