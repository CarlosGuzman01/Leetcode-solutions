class Solution:
    def customSortString(self, order: str, s: str) -> str:

        se = Counter(s)
        res = []

        for c in order:
            if c in se:
                for x in range(se[c]):
                    res.append(c)
            del se[c]
        
        for c in se:
            for x in range(se[c]):
                res.append(c)
        
        return "".join(res)

        