class Solution:
    def secondHighest(self, s: str) -> int:
        seen = set()
        res = []

        for c in s:
            if c.isdigit() and c not in seen:
                seen.add(c)
                res.append(int(c))

        if len(seen) < 2:
            return -1
        
        res.sort(reverse = True)

        return res[1]


        