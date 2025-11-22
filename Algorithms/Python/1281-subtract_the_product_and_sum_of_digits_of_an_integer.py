class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0

        for c in str(n):
            temp = int(c)
            product *= temp
          
            sum += temp
           
        return product - sum