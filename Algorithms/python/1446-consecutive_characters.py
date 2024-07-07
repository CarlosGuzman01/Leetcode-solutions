class Solution:
    def maxPower(self, s: str) -> int:
        temp = '@'
        counter = 1
        maxp = 0

        for c in s:
            if temp == c:
                counter += 1
            else:
                temp = c
                counter = 1
            
            maxp = max(counter, maxp)
        return maxp 



        