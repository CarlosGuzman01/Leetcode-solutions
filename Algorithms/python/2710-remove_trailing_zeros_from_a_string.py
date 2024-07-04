class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        n = int(num)

        while(True):

            if n % 10 != 0:
                break
            n //= 10

        return str(n)
        