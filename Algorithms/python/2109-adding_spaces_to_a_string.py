class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        res = []

        for i in range(len(s)):
            if j < len(spaces) and spaces[j] == i:
                j += 1
                res.append(" ")
            
            res.append(s[i])

        return "".join(res)
        