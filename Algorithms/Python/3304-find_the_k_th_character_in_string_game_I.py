class Solution:
    def kthCharacter(self, k: int) -> str:
        res = ['a']

        while len(res) < k:
            for i in range(len(res)):
                c = chr(ord(res[i]) + 1)
                res.append(c)
        return res[k - 1]




        