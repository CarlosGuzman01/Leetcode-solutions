class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        def rev(n):
            res = 0
            while n > 0:
                digit = n % 10
                res += digit
                res *= 10
                n //= 10
            res //= 10
            return res


        s = set()
        for n in nums:
            s.add(n)
            s.add(rev(n))
        
        return len(s)

        
        


        