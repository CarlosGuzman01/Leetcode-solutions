class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False
        if x < 0:
            negative = True
            x = -x
        
        rev = 0
        while x > 0:
            digit = x % 10
            
            if rev >= 2 ** 31 or rev <= -2 ** 31:
                return 0
            
            rev += digit
            rev *= 10
            x //= 10
        
        rev //= 10

        if negative:
            rev = -rev
        return rev


        
        








        
        