class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n == 0:
                continue
            s.add(n)
        return len(s)
        

        