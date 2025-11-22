class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        map = {}

        for i, c in enumerate(s):
            map[c] = i
        
        for i, c in enumerate(t):
            res += abs(map[c] - i)
        return res








        