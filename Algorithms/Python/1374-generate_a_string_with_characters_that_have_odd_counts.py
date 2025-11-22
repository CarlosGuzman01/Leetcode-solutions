class Solution:
    def generateTheString(self, n: int) -> str:
        s = n * 'a'

        if len(s) % 2 != 0:
            return s
        
        p = list(s)

        p[0] = 'b'

        return "".join(p)



        