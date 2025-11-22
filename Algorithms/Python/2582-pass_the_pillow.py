class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        i = 1
        p = 1
        boo = True

        while i <= time:
            if p == n or (p < 2 and i > 1):
                boo = not boo
            if boo:
                p += 1
            else:
                p -= 1
            i += 1
        return p
            
        
        