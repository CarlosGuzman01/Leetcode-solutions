class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def find(x):
            x = str(x)
            m = 0
            for c in x:
                m = max(m, int(c))
            return int(str(m) * len(x))

        
        total = 0
        for n in nums:
            total += find(n)
        return total
        
        



        