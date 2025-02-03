class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []

        for i in range(len(s)):
            if i % 2 == 0:
                res.append(s[i])
            else:
                n = int(s[i])
                val = ord(s[i - 1])
                p = val + n
                res.append(chr(p))

        return "".join(res)

        